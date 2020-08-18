import pycurl
from io import BytesIO 

def curlGet(URL):
    print(URL)
    b_obj = BytesIO() 
    crl = pycurl.Curl() 
    # Set URL value
    crl.setopt(crl.URL, URL)
    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)
    # Perform a file transfer 
    crl.perform() 

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()
    return get_body.decode('utf8')

def searchURL(data, key):
    key = '.'+str(key)+'.html'
    index = data.find(key)
    firstIndex = index
    while(firstIndex > 0):
        if(data[firstIndex]=='/'):
            break
        firstIndex -= 1
    return data[firstIndex:index]+key

def getLink(id):
    if(id[-1]=='\n'):
        id = id[:-1]
    data =curlGet('https://www.wg-gesucht.de/'+str(id)+'.html?campaign=suchauftrag_detail')
    return 'https://www.wg-gesucht.de/nachricht-senden' + searchURL(data, id)
