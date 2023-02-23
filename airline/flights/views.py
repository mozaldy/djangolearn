from django.shortcuts import render, redirect

from .models import Flight, Passenger
# Create your views here.
def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, pk):
    flight = Flight.objects.get(pk=pk)
    return render(request, 'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })

def book(request, pk):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=pk)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return redirect('flight', flight.id)