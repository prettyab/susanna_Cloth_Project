from django.shortcuts import render,redirect
from ClothApp.models import Product,Categories,Filter_Price,Contact


def base(request):
    return render(request,'base.html')


def index(request):
    # filter with status
    product = Product.objects.filter(status='published')   
    context = {'product': product}
    return render(request, 'index.html', context)




def product(request):
    product=Product.objects.filter(status='published')
    categories=Categories.objects.all()
    filterprice=Filter_Price.objects.all()

    CATID=request.GET.get('categories')
   

    from django.db.models import Q

    if CATID:
        product = Product.objects.filter(categories=CATID,status='published')
   
    else:
        product = Product.objects.filter(status='published')

    context={
        'product':product,
        'categories':categories,
        'filterprice':filterprice
    }
    return render(request,'product.html',context)



def search(request):
    query=request.GET.get('query')
    # print(query)
    product=Product.objects.filter(name__icontains=query)
    content={
        'product':product
    }
    return render(request,'search.html',content)



##########product detalis function##########
def product_detalis(request,id):
    prod=Product.objects.filter(id=id).first()
    context={
        'prod':prod,
    }

    return render(request,'product_detalis.html',context)



##CONTACT#########
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        return redirect('/')
    return render(request,'contact.html')

from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        customer = User.objects.create_user(username,email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()

        # Redirect to the 'index' view after successful registration
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the correct function name and pass the user object
            return redirect('/')
        else:
            # Handle the case where authentication fails
            return redirect('login')

    return render(request,'login.html')



def logout(request):
    auth_logout(request)
    return redirect('/')
    
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
    

# Create your views here.



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'card.html')


def cart_checkout(request):
    payment=client.order.create(
        {
            "amount":500,
            "currency":"INR",
            "payment_capture":'1'

        })
    
    order_id=payment['id']
    context={
        'order_id':order_id,
        'payment':payment,
    }

    
    return render(request,'checkout.html',context)

import razorpay
from razorpay import Client
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRECT))






def placeorder(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        uid=request.session.get('-auth_user_id')
        user=User.objects.get(id=uid)

        lastname=request.POST.get('lastname')
        country=request.POST.get('country')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        postcode=request.POST.get('postcode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        order_id=request.POST.get('order_id')
        payment=request.POST.get('payment')
        amount=request.POST.get('amount')
        order=Order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            country=country,
            address=address,
            city=city,
            state=state,
            postcode=postcode,
            phone=phone,
            email=email,
            payment_id=order_id,
            amount=amount,



        )
        order.save()
    return render(request,'placeout.html')






def receipt(request):
    totalAmount = calculateTotalAmount(request)  # Pass the request object to the function
    response = get_payment_response()  # Implement this function to get the Razorpay payment response

    context = {
        'totalAmount': totalAmount,
        'response': response,
    }

    return render(request, 'receipt.html', context)


def calculateTotalAmount(request):
    # Ensure that the quantities and prices are converted to integers before performing calculations
    totalAmount = 0
    for key, value in request.session.get('cart', {}).items():
        totalAmount += int(value['price']) * int(value['quantity'])
    return totalAmount

def get_payment_response():
    # Implement your logic to get the Razorpay payment response
    # This can include fetching data from the payment gateway or any other source
    # For demonstration purposes, a dummy response is returned
    return {
        'razorpay_payment_id': 'rzp_test_bdhXja6YIYa195',
        'razorpay_order_id': '5Saohy8E0RUb5WqdVpE7iUEc',
        
    }
