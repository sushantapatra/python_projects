from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator # this is only for custom function decorator
from django.views import View
# Create your views here.
from .models import Products
from .models import Category
from .models import Customer
from .models import Order
from .models import Post

from .middlewares.auth import auth_middleware

# print(check_password(
#     'pbkdf2_sha256$600000$HiUiuz8WZsHMkLCdzCdfaS$ikaBo9l0F34XwM0J1TfoOHzu52+/78HNUggtfoIpQlk=', '12345'))

""" Function Base Views"""


def index(request):
    catgory_id = request.GET.get('category')
    if catgory_id:
        productsObj = Products.getAllProductsById(catgory_id)
    else:
        productsObj = Products.getAllProducts()

    categoryObj = Category.getAllCategories()

    data = {
        'products': productsObj,
        'categories': categoryObj
    }
    # return render(request, 'orders/order.html', {'products': productsObj})
    return render(request, 'index.html', data)


def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    email = postData.get('email')
    phone = postData.get('phone')
    password = postData.get('password')
    hashPassword = make_password(password)
    # create instance
    customer = Customer(first_name=first_name, last_name=last_name,
                        email=email, phone=phone, password=hashPassword)

    isExists = customer.ifEmailExists()
    if isExists:
        messages.error(request, 'Email already exists!')
        return render(request, 'signup.html')

    customer.register()
    messages.success(request, 'User registrated successfully!')

    return redirect('homepage')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def loginUserFun(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    customerObj = Customer.getCustomerByEmail(email)
    if customerObj:
        decodePassword = check_password(password, customerObj.password)
        if decodePassword:
            # set session
            request.session['customer_id'] = customerObj.id
            request.session['customer_email'] = customerObj.email
            request.session['customer_phone'] = customerObj.phone
            request.session['customer_name'] = customerObj.first_name + \
                " " + customerObj.last_name
            return redirect('homepage')
        else:
            messages.error(request, 'Email or Password is invalid')
            return render(request, 'login.html')
    else:
        messages.error(request, 'Email or Password invalid')
        return render(request, 'login.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return loginUserFun(request)


def logout(request):
    request.session.clear()
    return redirect('login')


def posts(request):
    posts =Post.getAllPosts()
    return render(request, 'posts.html',{'posts':posts})



""" Class Base View
    => from django.views import View
    define URL =>path('login', Login.as_view(), name="login")
"""


class Login(View):
    returnUrl =None
    # override the get method
    def get(self, request):
        Login.returnUrl =request.GET.get('returnUrl')
        return render(request, 'login.html')

    # override the post method
    def post(self, request):
        return self.loginUser(request)

    def loginUser(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customerObj = Customer.getCustomerByEmail(email)
        if customerObj:
            decodePassword = check_password(password, customerObj.password)
            if decodePassword:
                # set session
                request.session['customer_id'] = customerObj.id
                request.session['customer_email'] = customerObj.email
                request.session['customer_phone'] = customerObj.phone

                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl) # only use to redirect http route like : /order
                
                Login.returnUrl=None
                return redirect('homepage') # only using to redirect route name like:order
            else:
                messages.error(request, 'Email or Password is invalid')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Email or Password invalid')
            return render(request, 'login.html')


class Signup(View):
    # ovverride the get method
    def get(self, request):
        return render(request, 'signup.html')

    # ovverride the post method
    def post(self, request):
        return self.registerUserData(request)

    # create register save function to save user

    def registerUserData(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        hashPassword = make_password(password)
        # create instance
        customer = Customer(first_name=first_name, last_name=last_name,
                            email=email, phone=phone, password=hashPassword)

        isExists = customer.ifEmailExists()
        if isExists:
            messages.error(request, 'Email already exists!')
            return render(request, 'signup.html')

        customer.register()
        messages.success(request, 'User registrated successfully!')

        return redirect('homepage')


class Index(View):
    def get(self, request):
        cartSession = request.session.get('cart')
        if not cartSession:
            request.session['cart'] = {}

        productsObj = None
        # request.session.clear('cart')  # clear session
        catgory_id = request.GET.get('category')
        # print(request.session.get('customer_email'))  # get email in session
        session_data = request.session
        # print(session_data.items())  # print all session data
        if catgory_id:
            productsObj = Products.getAllProductsById(catgory_id)
        else:
            productsObj = Products.getAllProducts()

        categoryObj = Category.getAllCategories()

        data = {
            'products': productsObj,
            'categories': categoryObj
        }
        # return render(request, 'orders/order.html', {'products': productsObj})
        return render(request, 'index.html', data)

    def post(self, request):
        productId = request.POST.get('product_id')  # GEt Post Data
        removeCart = request.POST.get('remove')  # GEt Post
        addCart = request.POST.get('add')  # GEt Post Data
        # Get session data and set Session Data
        cartSession = request.session.get('cart')
        if cartSession:
            quantity = cartSession.get(productId)
            if quantity and quantity != 'null':
                if removeCart is not None and int(removeCart) == 1:
                    if int(quantity) <= 1:
                        cartSession.pop(productId)
                    else:
                        cartSession[productId] = int(quantity) - 1
                else:
                    cartSession[productId] = int(quantity) + 1

                if addCart is not None and int(addCart) == 1:
                    cartSession[productId] = int(quantity) + 1
            else:
                cartSession[productId] = 1

        else:
            cartSession = {}
            cartSession[productId] = 1

        request.session['cart'] = cartSession

        return redirect('homepage')


class Cart(View):
    def get(self, request):
        carts = request.session.get('cart')  # Get all session data
        # print(carts)  # {'1': 1, '2': 1}
        # print(carts.keys())  # get all keys dict_keys(['1', '2'])
        # print(list(carts.keys()))  # convert to list ['1', '2']
        cartIdsStr = list(carts.keys())
        # Remove single quotes using list comprehension ['1', '2'] to [1, 2]
        cartIds = [int(s) for s in cartIdsStr]
        cartProducts = Products.getProductsByIds(cartIdsStr)
        # print(cartProducts)
        return render(request, 'cart.html', {"products": cartProducts})

    def post(self, request):
        pass


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_email = request.session.get('customer_email')
        customerObj = Customer.getCustomerByEmail(customer_email)
        carts = request.session.get('cart')
        productIds = list(carts.keys())
        cartProducts = Products.getProductsByIds(productIds)
        for product in cartProducts:
            order = Order(
                customer=customerObj, product=product,
                price=product.price, quantity=carts.get(str(product.id)),
                address=address,
                phone=phone
            )
            res = order.placeOrder()
            print(res)

        request.session.clear()
        return redirect('order')


class Orderlist(View):
    #@method_decorator(auth_middleware) #calling custom middleware
    def get(self, request):
        customer_email = request.session.get('customer_email')
        customerObj = Customer.getCustomerByEmail(customer_email)
        if customerObj:
            orders = Order.getOrdersByCustomer(customerObj)
        else:
            orders = {}
        return render(request, 'orders.html', {"orders": orders})
