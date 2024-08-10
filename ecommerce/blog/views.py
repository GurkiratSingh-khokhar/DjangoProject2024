from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from.models import *
from  django.conf import settings
import json
import razorpay
from django.views.decorators.csrf import csrf_exempt


def services(request):
    return render(request,'blog/services.html')

def events(request):
    return render('blog this is my events page')

def home(request):
    return render('blog this is my Home page')

def about(request):
    return render(request,'blog/about.html')

def blog(request):
    return render(request,'blog/blog.html')


def login(request):
    return render(request,'blog/login.html')

def signup(request):
    return render(request,'blog/signup.html')

def contact(request):
    return render(request,'blog/contact.html')







def trending_products(request):
    prod = product.objects.all()
    return render(request, 'blog/trend.html', {'prod': prod})

def trending_product_detail(request, pname):
        if product.objects.filter(name=pname):
            prod = product.objects.filter(name=pname).first()
            return render(request, 'blog/details.html', {'prod': prod})
        # return render(request, 'blog/details.html')


def category12(request):
    cat=category.objects.all()
    return render(request,'blog/index.html',{'cat': cat})

def product12(request,name):
    if category.objects.filter(name=name):
        prod=product.objects.filter(cat__name=name)[:3]
        return render(request,'blog/shop.html',{'prod': prod,'cate':name})
    return render(request, 'blog/shop.html')


def product_detail(request,cname,pname):
    if category.objects.filter(name=cname):
        if product.objects.filter(name=pname):
            prod=product.objects.filter(name=pname).first()
            return render(request,'blog/details.html',{'prod': prod})
        # return render(request, 'blog/details.html')
    return render(request, 'blog/details.html')


def registration12(request):
    if request.method=="POST":
        name = request.POST['user1']
        email12= request.POST['email1']
        password12= request.POST['password1']
        if registration.objects.filter(email=email12):
            msg = "you are already registered"
            return render(request, 'blog/signup.html', {'msg': msg})

        else:
            request.method == "POST"
            name = request.POST['user1']
            email12 = request.POST['email1']
            password12 = request.POST['password1']
            registration.objects.create(name=name, email=email12, password=password12)
            msg = "you are registered"
            return render(request, 'blog/signup.html', {'msg': msg})
    return render(request,'blog/signup.html')


def login12(request):
    if request.method=="POST":
        email12 = request.POST['email1']
        password12 = request.POST['password1']
        request.session['email'] = email12

        registration.objects.filter(email=email12,password=password12)
        if registration.objects.filter(email=email12,password=password12):
            msg = "login successfully"
            return redirect('index')
        else:
            msg = "please register"
            return render(request, 'blog/login.html', {'msg': msg})
    return render(request, 'blog/login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('index')


def create_session(request):
    msg="session created successfully"
    return render(request,"blog/index.html",{ 'msg':msg })

def call_session(request):
    em=request.session['email']
    if em:
        msg='session ok'
    else:
        msg='please login'
    return render(request,"blog/index.html",{ 'msg':msg })


# def addto_cart(request,id):
#     pid=product.objects.filter(id=id)
#     if'user'in request.session:
#         email12= request.session['email']
#         registration.objects.filter(email=email12)
#         user12=registration.objects.get(email=email12)
#         c1=cart(user=user12)
#         c1.prod.add(pid)
#         c1.save()
#     return render(request,'blog/cart.html')


def addto_cart(request,id):
    item= product.objects.get(id=id)
    if 'email' in request.session:
        email12= request.session['email']
        if registration.objects.filter(email=email12):
            user1= registration.objects.get(email=email12)
            c1 = Cart.objects.get_or_create(user=user1)[0]
            if item in c1.prod.all():
                msg3 = "item already exist."
                return redirect('viewcart')
            else:
                c1.prod.add(item)
                return redirect('viewcart')
        else:
            return HttpResponse("email not found.")
    elif 'email' not in request.session:
        return redirect('index')
    return render(request,"blog/cart.html")





# def delete_data(request,self):
#     item = product.objects.get(id=id)
#     if 'email' in request.session:
#         email12 = request.session['email']
#         if registration.objects.filter(email=email12):
#             user1 = registration.objects.get(email=email12)
#             product_id = str(product.id)
#             if product_id in cart:
#                 del cart[product_id]
#                 self.save()



def search(request):
    s1=request.GET['data']
    prod=product.objects.filter(name__icontains=s1)
    return render(request,'blog/search.html',{'prod':prod})


def search_product_detail(request,pname):
        if product.objects.filter(name=pname):
            prod=product.objects.filter(name=pname).first()
            return render(request,'blog/details.html',{'prod': prod})
        # return render(request, 'blog/details.html')



# def view_cart(request):
#     if "email" in request.session:
#         email12 = request.session['email']
#         if registration.objects.filter(email=email12):
#             email12 = registration.objects.get(email=email12)
#             cart1=cart.objects.get(user=email12)
#             c1=cartitem.objects.filter(cart=cart1)
#             c2=c1.all()
#             return render(request, "blog/cart.html",{'c2':c2})
#     return redirect('vcart')

def view_cart(request):
    if "email" in request.session:
        email12 = request.session['email']
        if registration.objects.filter(email=email12).exists():
            email12 = registration.objects.get(email=email12)
            c1 = Cartitem.objects.filter(cart__user=email12)
            cart2 = c1.all()
            total_price = sum(item.prods.price * item.quantity for item in c1)
            request.session['total_cost']=total_price
            item_data = [{
                'image':item.prods.image,
                'id': item.id,
                'product_name': item.prods.name,
                'quantity': item.quantity,
                'price': item.prods.price,
                'total': item.prods.price * item.quantity
            } for item in c1]
            return render(request, 'blog/cart.html',{'cart2': cart2,'total_price':total_price,'cart_items': item_data})
        else:
            msg="Item not exists"
            return render(request, 'blog/cart.html',{'msg',msg})
    return render(request, 'blog/cart.html')

# def view_cart(request):
#     if 'email' in request.session:
#         email12=request.session['email']
#         registration.objects.filter(email=email12)
#         email12 = registration.objects.get(email=email12)
#         request.session['user'] =email12
#         cart=Cart.objects.get(user=request.user)
#         cartitems=Cartitem.objects.filter(cart=cart)
#         return render(request,'blog/cart.html',{'cart':cart,'cartitems': cartitems})
#     return render(request,'blog/cart.html')
def delete_cart_item(request,id):
            item = Cartitem.objects.filter(id=id)
            item.delete()
            return redirect('viewcart')




def order_payment(request):
    if 'email' in request.session:
        total_price=request.session['total_cost']
        cu=request.session['email']
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment_order = client.order.create({"amount": int(total_price) * 100, "currency": "INR", "payment_capture": "1"})
        order = Order.objects.create(
            name=cu, amount=int(total_price), provider_order_id=payment_order["id"]
        )
        order.save()
        return render(
            request,
            "blog/payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/shop/callback/"+ cu,
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "blog/payment.html")


@csrf_exempt
def callback(request,id):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if  verify_signature(request.POST):


            order.status = PaymentStatus.SUCCESS

            order.save()

            return redirect("status")
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "blog/cart.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "blog/cart.html", context={"status": order.status})


def clear_cart(request):
    if "email" in request.session:
        email123 = request.session['email']


        if registration.objects.filter(email=email123).exists():

            user = registration.objects.get(email=email123)
            cart = user.cart_set.first()  # Assuming one cart per user

            if cart:

                items_deleted,_= Cartitem.objects.filter(cart=cart).delete()
    return redirect('viewcart')

# def total_price():
#     if


def add_quantity(request,id):
    c1 = Cartitem.objects.get(id=id)
    c1.quantity += 1
    c1.save()
    return redirect('viewcart')

def sub_quantity(request,id):
    c1 = Cartitem.objects.get(id=id)
    c1.quantity -= 1
    c1.save()
    return redirect('viewcart')

