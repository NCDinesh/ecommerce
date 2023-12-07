from django.shortcuts import render
from .models import product

def index(request):
    st=""
    data={}
    productdata = product.objects.all().order_by('-id')
    # if request.method=="POST":
    #     st=request.POST['servicename']
    #     if st!=None:
    #         servicedata = service.objects.filter(service_title__icontains=st)
    data={
        'productdata':productdata
    }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def cart(request):
    return render(request,"cart.html")

def sproduct(request):
    return render(request,"sproduct.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")




# Create your views here.
