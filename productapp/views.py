from django.views.generic.edit import View
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect


#def index(request):
   # return HttpResponse('Current Products %s.' % Product.name)


def index(request): #HTTPRequest / HTTPResponse
    return HttpResponse( "Hello World!." ) # no templates yet

