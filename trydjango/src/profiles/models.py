from django.db import models

# Create your models here.
class profile(models.Model):
	name=models.CharField(max_length=1200)
	description=models.TextField(default="this is a description aboout yourself")
	location =models.CharField(max_length=1200,blank=True)
	job=models.CharField(max_length=1200,null=True)

	def __unicode__(self):
		return self.name

