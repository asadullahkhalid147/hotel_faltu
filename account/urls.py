"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import  regisger,singout,login_veiw,profile,change_password
urlpatterns = [

path('register/', regisger, name='regisger'),
path('signout/', singout, name='singout'),
path('logoin/', login_veiw, name='login_veiw'),
path('profile/', profile, name='profile'),
path('change_password/', change_password, name='change_password'),



]
