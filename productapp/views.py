from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from productapp.forms import ProductForm
from productapp.models import Product


def product_list(request):
    products = Product.objects.all()  # select* from , delete , update
    print('*****************')
    return render(request, 'productapp/product_list.html', {'products': products, 'mydata': [1, 2, 3]})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'productapp/product_detail', {'product': product})

# def index(request):  # HTTPRequest / HTTPResponse
# return HttpResponse("Hello World!.")  # no templates yet
