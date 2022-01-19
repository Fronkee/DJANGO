from django.urls import path
from .views import *

urlpatterns = [ 
    path('',cats,name='cats'),
    path('subs/',subs,name='subs')
]