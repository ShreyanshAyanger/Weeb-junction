from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView


def home(request):
    return render(request,'blog/home.html')

def animelist(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'blog/list.html', context)

# def animepost(request):
# 	return render(request,'blog/animepost.html')

class PostDetailView(DetailView):
	model=Post
	template_name='blog/animepost.html'
		

def about(request):
    return render(request,'blog/about.html')

def contact(request):
	# if method=="POST":
		
    return render(request,'blog/contact.html')




# Create your views here.
