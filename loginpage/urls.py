from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from loginpage import views




urlpatterns = [
    
   path('',views.home,name="home"),
   path('signup',views.signup,name="signup"),
   path('log',views.log,name="log"),
   path('signin',views.signin,name="signin"),

   # Government site func
   path('iit',views.iit,name="iit"),
   path('AICTE',views.AICTE,name='AICTE'),
   path('NCS',views.NCS,name='NCS'),


   # Private site func
   path('TCS',views.TCS,name='TCS'),
   path('INFO',views.INFO,name='INFO'),
   
   path('signout',views.signout,name="signout"),

   path('passchange',views.passchange,name="passchange"),

   
   
]
