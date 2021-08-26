from django.shortcuts import render
from .models import Post


def home(request):
    return render(request,'blog/home.html')

def animelist(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'blog/list.html', context)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
	# if method=="POST":
		
    return render(request,'blog/contact.html')




# Create your views here.
