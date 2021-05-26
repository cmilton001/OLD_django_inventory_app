from typing import Any

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from productapp.forms import ProductForm
from productapp.models import Product


# class ProductList(ListView):
# template_name = 'productapp/product_list.html'
# model = Product
# context_object_name = 'products'

# def index(request : Any) :  # HTTPRequest / HTTPResponse
# return render(request, 'productapp/index.html')

def index(request):  # HTTPRequest / HTTPResponse
    return HttpResponse("Hello World!.")  # no templates yet
