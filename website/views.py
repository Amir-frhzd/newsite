from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    return render(request,'website/contact.html')

def work_view(request):
    return render(request,'website/work.html')

def blog_view(request):
    return render(request,'website/blog.html')



# Create your views here.
