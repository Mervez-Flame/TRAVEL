from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Flight, Booking
from django.http import HttpResponse 
from django.http import JsonResponse

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
    flights = Flight.objects.filter(is_cancelled=False)
    
    # if request.method == 'POST':
    #     origin = request.GET[origin]
    #     destination = request.GET['destination']
    
    # if destination in request.GET:
    #     keyword = request.GET[destination]
    #     if keyword:
    #         result = flights.objects.order_by('-created_date').filter(Q(destination_icontains=destination) | Q(here for origin_icontains=keyword))
    #         U can implement count  = result.count()
    # context = {
    #     'result':result,
    #     'count':count
    #     }

    #booking = Booking.objects.all() 
    # origin =  flights.origin
    # destination = flights.destination
    # departure_date = flights.departure_datenb
    # arrival_date = flights.arrival_date
    # price = flights.price
    # bookings = flights.bookings
    # slot_left = flights.slot_left
    # is_cancelled = flights.is_cancelled
    return render(request, 'Booking.html', {'flight' : flights},  )

# def Bookings(request):
#     if request.headers.get("x-requested-with") == "XMLHttpRequest" and request.method == "GET":
#         origin = request.GET.get("origin")
#         destination = request.GET.get("destination")
        
#         # Query the Flight model to get flight information
#         try:
#             flights = Flight.objects.get(origin=origin, destination=destination, is_cancelled=False)
#         except Flight.DoesNotExist:
#             return JsonResponse({"error": "Flight not found."}, status=404)
        
#         # Prepare the flight data as a JSON response
#         flight_data = {
#             "departure_date": flights.departure_date.strftime("%Y-%m-%d %H:%M:%S"),
#             "arrival_date": flights.arrival_date.strftime("%Y-%m-%d %H:%M:%S"),
#             "price": str(flights.price),
#             "bookings": str(flights.bookings),
#             "slot_left": str(flights .slot_left)
#         }
        
#         return JsonResponse(flight_data)
#     else:
#         return JsonResponse({"error": "Invalid request."}, status=400)
#     return redirect( 'home')



#flights = Flight.objects.filter(origin=origin, destination=destination, departure_date__gte=departure_date)
#return render(request, 'bookings/flight_search_results.html', {'flights': flights, 'num_passengers': num_passengers})arriva