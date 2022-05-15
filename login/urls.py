from django.urls import path
from .views import *

urlpatterns =[
    path('', login),
    path('signup/', signup),
    path('signin/', signin),
    path('signout/',signout),
    path('companyregister/', companysignup)
]