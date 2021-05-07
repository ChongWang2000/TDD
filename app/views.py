from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
from app.models import Item


def index(request):
    return render(request,'index.html')

def home_page(request):
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/app/home')

    items=Item.objects.all()
    return render(request,'home.html',{'items':items})