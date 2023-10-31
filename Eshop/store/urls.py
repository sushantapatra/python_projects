from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, signup, login, logout, Login, Signup, Index, Cart, Checkout, Orderlist,posts
from .middlewares.auth import auth_middleware

urlpatterns = [
    # Function Based View URl
    # path('', index, name="homepage"),
    # path('signup', signup, name="signup"),
    # path('login', login, name="login"),

    # Class Based View URl
    path('', Index.as_view(), name='homepage'),
    path('login', Login.as_view(), name="login"),
    path('signup', Signup.as_view(), name="signup"),
    path('logout', logout, name="logout"),
    path('cart', Cart.as_view(), name="cart"),
    path('checkout', Checkout.as_view(), name="checkout"),
    path('order', auth_middleware(Orderlist.as_view()), name="order"), # adding custom middleware
    path('post', posts, name='post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
