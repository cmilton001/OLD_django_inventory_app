from django.conf.urls import url
from django.urls import path

from productapp import views

app_name = 'productapp'

# #URLPatterns for function based views
urlpatterns = [
    #path('', views.ProductList.as_view(), name='product_list'),
    # path('<int:product_name>/', views.product_detail, name='product_detail'),
    path('index/', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
]
