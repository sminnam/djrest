from django.db import models

class MyFiles(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	#Mandatory fields
	customerId = models.CharField(max_length=100)
	msisdn=  models.CharField(max_length=100)
	docfile = models.FileField(upload_to='file/')
	legalFile =  models.FileField(upload_to='legals/')
