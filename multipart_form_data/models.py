from django.db import models

class MyFiles(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, default='default_value')
	#Mandatory fields
	customerId = models.CharField(max_length=100)
	MSISDN =  models.CharField(max_length=100)
	docfile = models.FileField(upload_to='file/')
