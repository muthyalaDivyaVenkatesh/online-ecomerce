from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import post 
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def  post_create(request):
	form =PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save( commit =False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context={
	"form": form,
	}
	return render(request,"post_form.html",context)


def post_home(request):
	return HttpResponse  ("<h1>HELLO</h1>")





def post_detail(request,id):
	instance =get_object_or_404(post,id=id)
	context ={
	'title':instance.name,
	'instance':instance
	}
	return render (request,"post_detail.html",context)


def post_list(request):
	quaryset_list= post.objects.all()
	paginator = Paginator(contact_list, 30) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

	context ={
	"object_list":quaryset,
	"title" :"list"
	}
	return render(request,"page_list.html",context)
	#return HttpResponse  ("<h>list</h1>")

def listing(request):
    contact_list = Contacts.objects.all()

    return render(request, 'list.html', {'contacts': contacts})

def post_update(request,id=None):

	instance =get_object_or_404(post,id=id)
	form =PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save( commit =False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())


	
	context ={
	'title':instance.name,
	'instance':instance,
	'form':form,
	}
	return render (request,"post_detail.html",context)

	


def post_delete(request):
	return HttpResponse  ("<h1>delete</h1>")


