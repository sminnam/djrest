import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from multipart_form_data.models import MyFiles
from multipart_form_data.serializers import MyFilesSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# Get an instance of a logger
logger = logging.getLogger(__name__)

@api_view(['GET','POST'])
def upload_form(request):
	if request.method == 'POST':
		instance = MyFiles(docfile=request.FILES['docfile'], title=request.DATA['title'])
		instance.save()
		return Response('uploaded')
		
	elif request.method == 'GET':
		files = MyFiles.objects.all()
		serializer = MyFilesSerializer(files)
		return Response(serializer.data)

@api_view(['POST','GET'])
def upload_multipart(request):
	if request.method == 'POST':
		logger.info('POST Request is  for customerId=%s, MSISDN=%s', request.DATA['customerId'], request.DATA['MSISDN'] )
		serializer = MyFilesSerializer(data=request.DATA, files=request.FILES)
		if serializer.is_valid():
			serializer.save()
			logger.info('File %s is saved/uploaded for customerId=%s, MSISDN=%s', request.DATA['title'], request.DATA['customerId'], request.DATA['MSISDN'] )			
			return Response(data=request.DATA, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
	elif request.method == 'GET':
		files = MyFiles.objects.all()
		serializer = MyFilesSerializer(files)
		return Response(serializer.data)
