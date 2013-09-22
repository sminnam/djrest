from django.db import models

class MyFiles(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	#Mandatory fields
	
	msisdn=  models.CharField(max_length=100)
	docType=  models.CharField(max_length=100)
	language= models.CharField(max_length=2)
	media = models.CharField(max_length=8)
	ban = models.CharField(max_length=9)
	format = models.CharField(max_length=8)
	jsonFile = models.FileField(upload_to='downloads/contracts/')
	contractFile = models.FileField(upload_to='downloads/contracts/')
	idFile =  models.FileField(upload_to='downloads/contracts/ids/')
