from django.urls import path, include
from . import views
app_name = 'products'
urlpatterns = [
    path('', views.product_list),
    path('<slug:slug>', views.product_details, name='product_details'),
]
