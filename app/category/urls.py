from django.urls import path
from .views import *

urlpatterns = [ 
    path('',home,name='home'),
    path('cats/',cats,name='cats'),
    path('cats/subs/',subs,name='subs'),
    path('subs/create',createSub,name='subs-create'),
    path('cats/create',createCat,name='cats-create')
]