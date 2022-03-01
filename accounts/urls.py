from django.urls import path,include
from django.conf import settings
from accounts import views
from django.conf.urls.static import static
urlpatterns = [

    path('', views.accounts, name ='accounts'),
    path('order', views.order, name ='order'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)