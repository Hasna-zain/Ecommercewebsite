from django.contrib import admin
from django.urls import path,include

from ecommerceapp import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]