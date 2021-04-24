from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from my_web_site.blogs.models import Post
from .models import Post

#def home(request):
#       return HttpResponse('<h1>My Blog Home Page </h1>')
#def about(request):
#        return HttpResponse('<h2>AboutUs Page</h2>')


"""posts =[{
        "title":"This is First Post",
        "author":"Ashish",
        "date_posted":datetime.now(),
        "content":"This is First Sample Post Content"
        },{
        "title":"This is Second Post",
        "author":"Rahul",
        "date_posted":datetime.now(),
        "content":"This is Second Sample Post Content"

        },{
        "title":"This is Third Post",
        "author":"Manish Rawal",
        "date_posted":datetime.now(),
        "content":"This is Third Sample Post Content"
        }]"""


def home(request):
        posts= Post.objects.all()
        #posts=Post.published.all()
        context ={
                'title':'My Home Page',
                'posts':posts,
        }
        return render(request,template_name='blogs/home.html',context=context)


def about(request):
        return render(request,'blogs/about.html')

# Create your views here.
