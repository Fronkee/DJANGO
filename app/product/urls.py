from django.urls import path
from . import views

urlpatterns = [
    path('',views.allProducts,name='all-product'),
    path('cartview/<str:item>',views.cartView,name='cart-view'),
]