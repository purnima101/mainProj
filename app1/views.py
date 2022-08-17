from django.shortcuts import render, HttpResponse
from app1.models import Contact
# Create your views here.

def index(request):
    context={
        'name':'Purnima'
    }
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')
    

def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phn=request.POST.get('phn')
        desc=request.POST.get('desc')
        address=request.POST.get('address')
        # posted=request.POST.get('posted')

        contact=Contact(name=name,email=email,phn=phn,address=address,desc=desc)
        contact.save()

    return render(request,'contact.html')
    