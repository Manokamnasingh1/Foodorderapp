from django.urls import path,include

from accounts import views

urlpatterns = [

    path('', views.accounts, name ='accounts'),
    path('order', views.order, name ='order'),
    

]