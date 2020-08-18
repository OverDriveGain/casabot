import smtplib
import time
import imaplib
import email
from sendBot import read_file
#configured to process email notifications from wg-gesucht.de
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "manar.zaboub.wg.suche" + ORG_EMAIL
FROM_PWD    = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
LAST_EMAIL_FILE='.last'
WG_IDS_FILE='.wgids'
EMAIL_TITLE='zu Ihrem Suchauftrag gefunden' # emails notification has this title
LINKS_SCHEMA='suchauftrag_detail'	#to grab the ad's id from the received email.
EMAILS_BACK = 30
def extract_ids(msg):
	
                    
	ids=[]
	lines=msg.split('\n')
	for line in lines:
		if LINKS_SCHEMA in line:
			newLine=line.split('.de/')
			ids.append(newLine[1][0:7])
	print (ids)
	with open(WG_IDS_FILE,'a') as infile:
		for i in ids:
			infile.write(i)
			infile.write('\n')
def read_mail():
    new = False
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        new=False
        with open(LAST_EMAIL_FILE,'r') as infile:
              for line in infile:
                   if latest_email_id!=line and line!="":
                          first_email_id=int(line)
                   else:
                          print("no New Email")
        infile.close()
        if(first_email_id==1):	#when runing the first time
                first_email_id=latest_email_id-EMAILS_BACK
        for i in range(latest_email_id,first_email_id, -1):		
            typ, data = mail.fetch(str(i),'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    if EMAIL_TITLE in email_subject:
                    	new=True
                    	extract_ids(msg.get_payload())
                    email_from = msg['from']
                    print ('From : ' + email_from + '.....:')
                    print ('Subject : ' + email_subject + '\n')
        with open(LAST_EMAIL_FILE, 'w') as infile:
                print(latest_email_id)
                infile.write(str(latest_email_id))
        infile.close()
        
    except Exception as e:
    	print (str(e))
    return new

while(True):
	if(read_mail()):
		read_file()
		
	time.sleep(2.0)
	
