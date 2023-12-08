from django.shortcuts import render
from .models import product,newarrival
from django.core.paginator import Paginator
def index(request):
   
    data={}
    productdata = product.objects.all().order_by('-id')
    new = newarrival.objects.all().order_by('-id')

   
    data={
        'productdata':productdata,
        'new':new,
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
    data={}
    productdata = product.objects.all().order_by('-id')
    new = newarrival.objects.all().order_by('-id')
    
    paginator=Paginator(productdata,3)
    page_number=request.GET.get('page')
    productdatafinal=paginator.get_page(page_number)
    totalpage=productdatafinal.paginator.num_pages

   
    data={
        'productdata':productdatafinal,
        'new':new,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)] 

    }
    return render(request,"shop.html",data)




# Create your views here.
