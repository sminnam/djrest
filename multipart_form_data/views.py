import logging
import time
from StringIO import StringIO
from django.core.files import File
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from multipart_form_data.models import MyFiles
from multipart_form_data.serializers import MyFilesSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


# Get an instance of a logger
logger = logging.getLogger(__name__)


#@api_view(['GET','POST'])
#def upload_form(request):
#	if request.method == 'POST':
#		instance = MyFiles(conractFile=request.FILES['contractFile'])
#		instance.save()
#		return Response('uploaded')
#		
#	elif request.method == 'GET':
#		files = MyFiles.objects.all()
#		serializer = MyFilesSerializer(files)
#		return Response(serializer.data)

@api_view(['POST','GET'])
def upload_multipart(request):
	"""
    A view that can accept POST requests with JSON and content.
    """
	if request.method == 'POST':
		logger.debug('Received POST request')
		file_obj = request.FILES['jsonFile']
		#print file_obj.name, file_obj.size
		content = file_obj.read()
		stream = StringIO(content)
		jsonData = JSONParser().parse(stream)
		logger.debug(u'JSON data: {0}'.format(jsonData))
		serializer = MyFilesSerializer(data=jsonData, files=request.FILES)
		if serializer.is_valid():
			serializer.save()
			logger.info('File %s is saved/uploaded',request.FILES['contractFile'])
			result = generate_response(jsonData)
			return Response(data=result, status=status.HTTP_201_CREATED)
		else:
			logger.error('Invalid POST Request %s', request.DATA)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
	elif request.method == 'GET':
		files = MyFiles.objects.all()
		serializer = MyFilesSerializer(files)
		return Response(serializer.data)

def generate_response(data):
	"""
	 Tets generation of docid
	"""
	msisdn = data['msisdn']
	docId = str(int(time.time()))
	docId += msisdn 
	return {"msisdn":msisdn, "docId":docId}
	
