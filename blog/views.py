from django.shortcuts import render
from .models import Post, Contact_form
from django.views.generic import DetailView
from django.contrib import messages


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
	# if method=="POST
	# Name=models.CharField(max_length=30)
	# email=models.EmailField(max_length=35)
	# date_posted=models.DateTimeField(default=timezone.now)
	# phone_num=models.IntegerField()
	# message = models.TextField(max_length="200",)
	# # ":
	if request.method == 'POST':

		data=Contact_form()
		data.Name= request.POST.get('Name')
		data.email= request.POST.get('email')
		data.phone_num= request.POST.get('phone_num')
		data.message= request.POST.get('message')
		data.save()
		messages.success(request, 'Form submission successful')
		return render(request,'blog/submitted.html')
	else:
		return render(request,'blog/contact.html')
		
    




# Create your views here.
