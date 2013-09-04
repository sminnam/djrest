from django.db import models

class MyFiles(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, default='default_value')
	customerId = models.CharField(max_length=100, default='customernone')
	MSISDN =  models.CharField(max_length=100, default='0000000000000')
	docfile = models.FileField(upload_to='file/')
