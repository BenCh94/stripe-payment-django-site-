"""auth_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello import views as hello_views
from auth_app import views as auth_app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^register/$', auth_app_views.register, name='register'),
    url(r'^profile/$', auth_app_views.profile, name='profile'),
    url(r'^login/$', auth_app_views.login, name='login'),
    url(r'^Logout/$', auth_app_views.logout, name='logout'),
    url(r'^cancel_subscription/$', auth_app_views.cancel_subscription, name='cancel_subscription'),
    url(r'^banana123/$', auth_app_views.subscription_webhook),
]
