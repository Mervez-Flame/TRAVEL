from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Flight, Booking
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request, 'home.html')

def loginPage (request):
    return render(request, 'loginPage.html')

def contact(request):
    return render(request, 'contact.html')

def logout (request):
    auth.logout(request)
    return render(request, 'home')

def login (request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Logged In Succesfully")
        return redirect('home')
    else:
        messages.error(request, "Wrong username or password")
        return redirect('loginPage')
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirmPassword = request.POST.get('password2')

        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                messages.success(request, 'Signup Successfully')
                return redirect('loginPage')
        else:
            messages.error(request, 'Password not the same')
            return redirect('signUpPage')
    else:
        return render(request, 'signUpPage.html')
    
def signUpPage(request):
    return render(request, 'signUpPage.html')

def register(request):
    return render(request, 'register.html')

def booking(request):
    return render(request, 'Booking.html')

def Bookings(request):
    flight = Flight()
    booking = Booking()
    
    #if request.method == 'POST':

    booking.origin = flight.origin
    booking.destination = flight.destination
    booking.departure_date = request.GET['departure_date']
    booking.num_passengers = request.GET['num_passengers']
    return redirect( 'home')
#else:
    print("it didt work")



#flights = Flight.objects.filter(origin=origin, destination=destination, departure_date__gte=departure_date)
#return render(request, 'bookings/flight_search_results.html', {'flights': flights, 'num_passengers': num_passengers})