djrest: Multipart Upload

Note: To update LOCALE source in bash

export LANG="en_US.UTF-8"
export LC_COLLATE="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
export LC_MESSAGES="en_US.UTF-8"
export LC_MONETARY="en_US.UTF-8"
export LC_NUMERIC="en_US.UTF-8"
export LC_TIME="en_US.UTF-8"
export LC_ALL=






1. Testing
curl -i -F customerId=123456 -F MSISDN=2345677 -F title=cmis-article.pdf -F docfile=@Desktop/Orange/CMIS/cmis-article.pdf  http://localhost:8000/rsttodcf/upload/

2. Enable authentication. Add DEFAULT_PERMISSION_CLASSES to REST_FRAMEWORK directive in settings.py
http://django-rest-framework.org/api-guide/permissions.html

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    
    or
     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),

3. Set the downloaded files in settings file
E.g
MEDIA_ROOT = '/tmp/djrest/'
     

3. Testing with multiple files
curl -i  -F contractFile=@./testfiles/cmis-article.pdf -F jsonFile=@./testfiles/t.json  -F idFile=@./testfiles/o.xml -u qvantel:qvantel1234  -H 'Accept: application/json; indent=4' http://localhost:8000/api/documentum/pos 

HTTP/1.0 201 CREATED
Date: Fri, 06 Sep 2013 18:46:49 GMT
Server: WSGIServer/0.1 Python/2.7.1
Vary: Accept, Cookie
Content-Type: application/json; indent=4; charset=utf-8
Allow: POST, OPTIONS, GET

{
    "msisdn": "0567727727727277", 
    "docId": "2345667"
}


4. Using requests

import requests

url = 'http://localhost:8000/api/documentum/pos'
s = requests.Session()
s.auth = ('qvantel', 'qvantel1234')
files = {'contractFile': open('../testfiles/cmis-article.pdf', 'rb'), 'idFile':open('../testfiles/o.xml', 'rb') , 'jsonFile': open('../testfiles/t.json', 'rb')}
result = s.post(url, files=files)
print result.content
