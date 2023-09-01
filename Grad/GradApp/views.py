from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Flight, Booking
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request, 'home.html')

def loginPage (request):
    return render(request, 'login_view.html')

def contact(request):
    return render(request, 'contact.html')

def logout (request):
    auth.logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')  # Use get() to safely get the POST data
        password = request.POST.get('psw')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect('home')
        else:
            messages.error(request, "Wrong username or password")
            return redirect('loginPage')  # Make sure 'loginPage' is a valid URL name
    return redirect('home')

def signUpPage(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                return redirect('loginPage')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request , 'register.html') 

def booking(request):
    flights = Flight.objects.all()
    #booking = Booking() 
    # origin =  flights.origin
    # destination = flights.destination
    # departure_date = flights.departure_date
    # arrival_date = flights.arrival_date
    # price = flights.price
    # bookings = flights.bookings
    # slot_left = flights.slot_left
    # is_cancelled = flights.is_cancelled
    return render(request, 'Booking.html', {'flight' : flights},  )

def Bookings(request):
    # flight = Flight()
    # booking = Booking()

    # booking.origin =
    # booking.destination = flight.destination
    booking.departure_date = request.GET['departure_date']
    booking.num_passengers = request.GET['num_passengers']
    return redirect( 'home')



#flights = Flight.objects.filter(origin=origin, destination=destination, departure_date__gte=departure_date)
#return render(request, 'bookings/flight_search_results.html', {'flights': flights, 'num_passengers': num_passengers})arriva