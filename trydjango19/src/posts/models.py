from django.db import models

# Create your models here.
class post(models.Model):

	name = models.CharField(max_length=1200)
	Description =models.TextField(default="default secription")
	Location =models.CharField(max_length=1200,default='My_location')
	#Startdate = models.DateField(_("Date"), default=date.today)
	#enddate = models.DateField(_("Date"), default=date.today)
	Startdate = models.DateField(blank=True,null=True)
	endtdate = models.DateField(blank=True,null=True)
	MYCHOICES = (
        ('comdey', 'comdey'),
        ('adventure', 'adventure'),
        ('action', 'action'),
        ('horror', 'horror'))
	categories= models.CharField(max_length=100, choices=MYCHOICES,default="True",)
	
	published = models.BooleanField()
	profile_image = models.FileField( blank=True, null=True)

	def get_absoulte_url(self):
		return reverse("posts:detail",kwargs={"id":self.id} )
	
	class Mesta:
		ordering = ["-startdate","-updated"]




