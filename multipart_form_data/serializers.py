import logging
from django.forms import widgets
from rest_framework import serializers
from multipart_form_data.models import MyFiles
from multipart_form_data.documentum import Documentum

loggers = logging.getLogger(__name__)

class MyFilesSerializer(serializers.ModelSerializer):
	
	def validate(self, attrs):
		
		loggers.debug('Validating input')
		#To-Do: These field existence are already validated in Models. Valid values needs to be checked here
		if attrs['msisdn'] and attrs['contractFile'] and attrs['idFile'] and attrs['docType']:
			for key, value in attrs.iteritems():
				loggers.debug(u'{0} = {1}'.format(key, value))
			return attrs
		else:
			raise serializers.ValidationError("Invalid values in request")
		
	
	def save_object(self,obj):
		"""
		 Send files to documentum and if fails, save it to file systems in failed_dir
		"""
		x = Documentum()
		x.send_files()
		loggers.debug(u'serializer data is {0}'.format(self.data))
		obj.save()
		return self.object
	
	
	class Meta:
		model = MyFiles
		fields = ('msisdn', 'docType', 'format', 'language', 'ban', 'media','contractFile', 'idFile')
		#read_only_fields = ('msisdn','docType')
	
	
