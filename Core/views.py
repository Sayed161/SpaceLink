from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Company.models import RoleRequest,Location
from Office.models import Office,Desk,Room,TimeSlot
# Create your views here.
def home(request):
     approved_role_requests = RoleRequest.objects.filter(status='approved')
     for role_request in approved_role_requests:
        role_request.approve() 
     return render(request, 'home.html')

def index(request):
     approved_role_requests = RoleRequest.objects.filter(status='approved')
     for role_request in approved_role_requests:
        role_request.approve() 
     return render(request, 'index.html')

def solutions(request):
     approved_role_requests = RoleRequest.objects.filter(status='approved')
     for role_request in approved_role_requests:
        role_request.approve() 
     return render(request, 'solutions.html')

def office(request):
     offices = Office.objects.all() 
     city = request.GET.get('city')
     locations = Location.objects.all()
     if city:
          offices = offices.filter(company__Location__name=city)  # Using `__in` for the Location filter
     return render(request, 'office.html', {'office': offices,'locations': locations, 'city': city})

def room(request):
     rooms = Room.objects.all()
     city = request.GET.get('city')
     locations = Location.objects.all()
     if city:
          rooms = rooms.filter(company__Location__name=city)  # Using `__in` for the Location fil
     for room in rooms:
        room.slots = room.timeslot_set.all()
     return render(request, 'room.html', {'rooms': rooms,'locations': locations, 'city': city})

def desk_list(request):
    desks = Desk.objects.all()
    city = request.GET.get('city')
    locations = Location.objects.all()
    if city:
        desks = desks.filter(company__Location__name=city)  # Using `__in` for the Location filter
    return render(request, 'desk_list.html', {'desks': desks,'locations': locations, 'city': city})

