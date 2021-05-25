from django.urls import path

from productapp import views

app_name='productapp'
# #URLPatterns for function based views
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    ]