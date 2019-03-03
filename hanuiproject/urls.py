"""hanuiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import blog.views
import accounte.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# django.contrib.auth.views.LoginView

admin.autodiscover()
app_name = 'blog'
urlpatterns = [
    path('', blog.views.blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounte/', include('accounte.urls')),
    path('accounte/', include('django.contrib.auth.urls')),
    # path('', views.blog.blog, name='blog'),
    path('accounts/', include('allauth.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog'))
    # url(r'^blog/', include(blog_urls, namespace='blog')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
