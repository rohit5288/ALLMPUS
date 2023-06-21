from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import products,rfq
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

#from .forms import getquote
# Create your views here.
@login_required(login_url='/user/login') 
def home(request):
    image=products.objects.order_by('?')[:3]
    user=request.user
    return render(request,'products/product_home.html',{'product_obj':image,'user':user})

def product_page(request):
    product_obj=products.objects.order_by('product')
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return render(request,'products/product_page.html',{'product_obj':product_obj,'alpha':alpha})

def filter_prod(request,key):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    product_obj=products.objects.filter(product__startswith=key)
    return render(request,'products/product_page.html',{'product_obj':product_obj,'alpha':alpha})
    
def single_prod(request,pid):
    product_obj=products.objects.filter(id=pid)
    return render(request,'products/single_product.html',{'product_obj':product_obj})

def request_quote(request,pid):
    if request.method=="POST":
        data=request.POST
        name= data.get('name')
        email= data.get('email')
        company= data.get('company') 
        contact= data.get('contact')
        package= data.get('package')
        package_unit=data.get('package_unit')
        prod=products.objects.get(id=pid).product
        rfq.objects.create(
            product_id=products.objects.filter(id=pid)[0],
            name=name,
            email=email,
            company=company,
            contact=contact,
            package=package,
            package_unit=package_unit,
        )
        messages.success(request,'Hi {0}, We will provide you requested quotation shortly!'.format(name))
        send_mail(
            'Quotation Request Submitted Successfully!','Hi! {2}, We are grateful to do business with {3}.We will provide quotation for following product: {4} for {0} {1} quantity shortly.'.format(package,package_unit,name,company,prod),
            'saranrohit11@gmail.com',[email])
        send_mail('Request for Quotation','Send quotation to {0} at {1} for : PRODUCT: {4} for {2} {3} quantity.'.format(name,email,package,package_unit,prod),
                  'saranrohit11@gmail.com',['saranrohit01@gmail.com'])
    return render(request,'products/requestquote.html')
