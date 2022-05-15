from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.module_loading import import_string
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime as dt
from .models import *
from .scripts import *

#INDEX PAGES#

def index(request):
    return render(request, 'index.html')

def aboutpage(request):
    return redirect('https://albatross.travel')

def hotelindex(request):

    hotels = Hotel.objects.all()

    return render(request, 'hotelindex.html', {"Hotels":hotels})

#TEMPLATE RENDERING#

def profilepage(request, username):
    
    user = User.objects.get( username = username )
        
    if user.is_staff == 0:

        reservations = user.reservation_set.all()

        return render(request,'profile.html', {"User":user, "Reservations": reservations})
    
    else:
        company = Company.objects.get( name = username )
        Hotels  = company.hotel_set.all()
        reservations = Reservation.objects.filter(company = company.name)
        return render(request,'hotelmanager.html', {"Company":company, "Hotels":Hotels, "Reservations":reservations})

def hotelpage(request, hotelname, username):

    
    user        = User.objects.get(username=username)
    hotel       = Hotel.objects.get(name=hotelname)
    roomtypes   = hotel.roomtype_set.all()
    company     = Company.objects.get(id = hotel.company_id)
    admin       = False

    if user.is_staff == 1 and user.id == company.manager_id:
        admin = True

    elif user.is_staff == 1:
        return render('/')

    return render(request, 'hoteldisplay.html',  {"Hotel": hotel, "User":user ,"Admin":admin,"RoomTypes":roomtypes} )

def reservationpage(request, hotelname, categoryid, username):

    user        = User.objects.get(username=username)
    hotel       = Hotel.objects.get(name=hotelname)
    roomtype    = RoomType.objects.get(id=categoryid)
    company     = Company.objects.get(id = hotel.company_id)

    return render(request, 'reservationpage.html', {"Hotel":hotel, "User":user, "RoomType":roomtype, "Company":company})

# RESERVATION MANAGING #

def makereservation(request, hotelname, categoryid, username):

    user        = User.objects.get(username=username)
    hotel       = Hotel.objects.get(name=hotelname)
    company     = Company.objects.get(id = hotel.company_id)
    roomtype    = RoomType.objects.get(id=categoryid)
    date_start  = request.POST.get('date_start')
    date_end    = request.POST.get('date_end')

    Reservation.objects.create(
        company         = company.name,
        hotel_name      = hotel.name,
        roomtype        = roomtype.category,   
        user            = user,
        customer        = user.username,
        customer_email  = user.email,
        customer_fn     = user.first_name,
        customer_ln     = user.last_name,
        date_start      = date_start,
        date_end        = date_end,
        date_update     = dt.today().strftime('%Y-%m-%d'),
        date_created    = dt.today().strftime('%Y-%m-%d'))

    return redirect('/profile/%s'%(user.username))

def reservationupdate(request, id):

    reservation = Reservation.objects.get(id=id)
    company = Company.objects.get(name = reservation.company)
    statusupdate = bool(request.POST.get('statuspudate'))
    reservation.status = statusupdate
    reservation.save()

    return redirect('/profile/%s'%(company.name)) 

# CREATE AND DELETE MANAGEMENT #

def create(request, item):
    
    if item == "<Hotel>":
        company_name    = request.POST.get('company_name')
        company_id      = request.POST.get('company_id')
        name            = request.POST.get('name')
        location        = request.POST.get('location')
        description     = request.POST.get('description')
        image           = request.POST.get('image')
        
        Hotel.objects.create(name=name, location=location, description=description,image=image,company_id=company_id)
        
        messages.success(request, "Hotel registered succesfully")
        
        return redirect('/profile/%s'%(company_name))

    if item == "<RoomType>":
        company_name    = request.POST.get('company_name')
        hotel_name      = request.POST.get('hotel_name')
        hotel_id        = request.POST.get('hotel_id')
        category        = request.POST.get('category')
        cost            = request.POST.get('cost')
        description     = request.POST.get('description')
        image           = request.POST.get('image')

        RoomType.objects.create(category=category,description=description,cost=cost,hotel_id=hotel_id,image=image)

        messages.success(request, "Room Type created succesfully")
        
        return redirect('/view/%s/hotels/%s'%(company_name,hotel_name))
  
def delete(request, item):
    
    if item == "<Hotel>":
        company_name    = request.POST.get('company_name')
        name            = request.POST.get('name')

        hotel = Hotel.objects.get(name = name)        
        hotel.delete()        
        messages.success(request, "Hotel deleted succesfully")
        
        return redirect('/profile/%s'%(company_name))
    
    if item == "<RoomType>":
        company_name    = request.POST.get('company_name')
        hotel_name      = request.POST.get('hotel_name')
        category        = request.POST.get('category')

        roomtype = RoomType.objects.get(category = category)        
        roomtype.delete()        
        messages.success(request, "Hotel deleted succesfully")
        
        return redirect('/view/%s/hotels/%s'%(company_name,hotel_name))