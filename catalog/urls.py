from django.urls import path
from .views import home, checkout, product


urlpatterns = [
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/', product, name='product')
]