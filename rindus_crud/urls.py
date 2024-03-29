"""rindus_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import UsersList, CreateUser, UpdateUser, DeleteUser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^add/', CreateUser.as_view(), name='add'),
    url(r'^update/(?P<pk>\d+)/$', UpdateUser.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteUser.as_view(), name='delete'),
    url(r'^$', UsersList.as_view(), name='home'),
]
