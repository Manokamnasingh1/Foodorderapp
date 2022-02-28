
from django.shortcuts import render
from django.conf import settings

def accounts(request):
    return render(request, 'index.html') 
def order(request):
    return render(request, 'order.html')
