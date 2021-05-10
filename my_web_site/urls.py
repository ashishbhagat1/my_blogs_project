"""my_web_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include  # include for blogs applictions

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # this is for superadmin page show for login
    # path('blog/',include('blogs.urls')), # this is in blogs/urls.py inculude from blogs appliction
    path("posts/", include("blogs.urls")),
    # on localhost show First page this is in blogs/urls.py inculude from blogs appliction localhost:8000/posts
    path("accounts/", include("accounts.urls")),
    path("__debug__/", include(debug_toolbar.urls)),  # for debug tool
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# designing of Admin Pannel
admin.site.site_header = "Ashish Admin"
admin.site.site_title = "Ashish Admin Portal"
admin.site.index_title = "Welcome to Ashish Researcher Portal"
