from django.contrib import admin

# Register your models here.
from .models import post

class PostModelAdmin(admin.ModelAdmin):
	list_display =["name","Location"]
	list_filter =["Startdate","endtdate"]
	list_editable = ["name"]
	serch_fields =["name","Description"]
	class Meta:
		model = post


admin.site.register(post, PostModelAdmin)