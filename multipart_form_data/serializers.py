from django.forms import widgets
from rest_framework import serializers
from multipart_form_data.models import MyFiles

class MyFilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyFiles
		fields = ('docfile', 'legalFile','customerId', 'msisdn')


