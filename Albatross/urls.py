from django.contrib import admin
from django.urls import path, include
from Hotels.views import *
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('hotels/', hotelindex),
    path('about/', aboutpage),
    path('login/', include('login.urls')),
    path('view/<username>/hotels/<hotelname>', hotelpage),
    path('reservationpage/<hotelname>/<categoryid>/<username>', reservationpage),
    path('makereservation/<hotelname>/<categoryid>/<username>', makereservation),
    path('reservationupdate/<id>',reservationupdate),
    path('create/<item>', create),
    path('delete/<item>', delete),
    path('companysignup/', companylogin),
    path('profile/<username>', profilepage)
]
