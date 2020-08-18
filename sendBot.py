from curl import getLink
from doer import doThis
SEND_MSG_URL='https://www.wg-gesucht.de/nachricht-senden.html?message_ad_id='
ALREADY_SENT_SYMBOLE='x'
WG_ID_FILE='.wgids'
WG_ID_SENT_FILE='.wgidsent'
def rewrite_file(ids):
	with open(WG_ID_SENT_FILE,'a') as infile:
		infile.write(str(ids))
		#infile.write('\n')
def check_if_sent(sent_id):
	with open(WG_ID_SENT_FILE,'r') as infile:
		for line in infile:
			if int(line)==int(sent_id):
				return True
	return False

def read_file():
	ids=[]
	with open(WG_ID_FILE,'r') as infile:
		for line in infile:
			ids.append(line)
	ids=set(ids)
	idset=[]
	for id in ids:
		idset.append(id)

	for i in range(0,len(idset)):
		if check_if_sent(idset[i]):
			print(idset[i])
		else:
#			x=urllib2.urlopen(''.join([SEND_MSG_URL,idset[i]])).read()
			if doThis(getLink(idset[i])):
				rewrite_file(idset[i])	#this means mark wg id as sent.
