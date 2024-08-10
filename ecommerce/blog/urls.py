"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.signup),
    path('login/', views.login12, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.registration12, name="register"),
    path('cart/<int:id>', views.addto_cart, name="cart"),
    path('search/',views.search,name="search"),
    path('contact/', views.contact,name="contact"),
    path('aboutus/', views.about,name="about"),
    path('blog/', views.blog,name="blog"),
    path('services/', views.services,name="services"),
    path('detail/<str:cname>/<str:pname>', views.product_detail,name="productdetail"),
    path('detail/<str:pname>', views.search_product_detail,name="searchproductdetail"),
    path('create/', views.create_session),
    path('index/', views.category12,name='index'),
    path('products/<str:name>', views.product12,name="products"),
    path('delete/<int:id>',views.delete_cart_item,name="delete_item"),
    path('Clearcart/',views.clear_cart,name="Clearcart"),
    path('cart/',views.view_cart,name="viewcart"),
    path('trendingproducts/',views.trending_products,name="trendingproduct"),
    path('trendingproduct/<str:pname>',views.trending_product_detail,name="trendproduct"),
    path('orderpayment/',views.order_payment,name="orderpayment"),
    path('ADDITEM/<int:id>',views.add_quantity,name="ADDITEM"),
    path('SUBITEM/<int:id>',views.sub_quantity,name="SUBITEM"),


]
