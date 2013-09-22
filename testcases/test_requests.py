import requests

url = 'http://localhost:8000/api/documentum/pos'
s = requests.Session()
s.auth = ('qvantel', 'qvantel1234')
files = {'contractFile': open('../testfiles/cmis-article.pdf', 'rb'), 'idFile':open('../testfiles/o.xml', 'rb') , 'jsonFile': open('../testfiles/t.json', 'rb')}
#s.headers.update({'Accept: application/json'})
result = s.post(url, files=files)
print result.content

