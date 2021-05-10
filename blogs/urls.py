from django.urls import path
from . import views

# app_name = "blogUrl"

urlpatterns = [
    #path("", views.home, name="blog-home"),
    path("",views.post_list_view,name="blog-home"), # class views call instead of views.home function
    path('<int:pk>/',views.post_detail_view , name='post-detail'),
    path("about/", views.about, name="blog-about"),
]
