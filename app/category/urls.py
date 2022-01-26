from django.urls import path
from .views import *

urlpatterns = [ 
    path('',home,name='home'),
    path('cats/',cats,name='cats'),
    path('cats/create',createCat,name='cats-create'),
    path('cats/<int:id>/delete',catDelete,name='cat-delete'),
    path('cats/<int:id>/edit',catEdit,name='cat-edit'),
    
    #SubCategory
    path('cats/subs/',subs,name='subs'),
    path('subs/create',createSub,name='subs-create'),
    path('subs/<int:id>/delete',subDelete,name='sub-delete'),
    path('subs/<int:id>/edit',subEdit,name='sub-edit')

]