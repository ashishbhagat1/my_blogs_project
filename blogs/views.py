from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from my_web_site.blogs.models import Post
from .models import Post
from django.urls import reverse
from django.views.generic import CreateView, DeleteView,UpdateView,ListView,DetailView
# from hitcount.views import HitCountDetailView
# def home(request):
#       return HttpResponse('<h1>My Blog Home Page </h1>')
# def about(request):
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

# home function or PostListView work same we can use any one call from urls.py
def home(request):
    posts = Post.objects.all()
    # posts=Post.published.all()
    context = {
        "title": "My Home Page",
        "posts": posts,
    }
    return render(request, template_name="blogs/home.html", context=context)


def about(request):
    return render(request, "blogs/about.html")


# Create your views here. # Class Views
class PostListView(ListView):
    model = Post
    queryset = Post.published.all() # query call for all published record show
    template_name = "blogs/home.html"
    context_object_name = "posts"
    ordering = "-published_at"

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data= super().get_context_data()
        context_data['title'] = "BLOG HOME PAGE"
        return context_data

        #def get_queryset(self):
        #    qs = super().get_queryset()
        #    return qs.filter(status="published")

post_list_view = PostListView.as_view() #  this variable for use where required to show as view


class Post_Detail_View(DetailView):
    model = Post

post_detail_view = Post_Detail_View.as_view()