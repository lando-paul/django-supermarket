from django.urls import path
from .views import (
    HomeView,
    checkout,
    ProductDetail,
    add_to_cart,
    remove_from_cart
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ProductDetail.as_view(), name='product')
]