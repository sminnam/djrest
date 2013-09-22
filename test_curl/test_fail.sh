#!/bin/sh

curl -i   -F contractFile=@../testfiles/cmis-article.pdf -F jsonFile=@../testfiles/fail.json  -F idFile=@../testfiles/o.xml -u qvantel:qvantel1234  -H 'Accept: application/json; indent=4' http://localhost:8000/api/documentum/pos
