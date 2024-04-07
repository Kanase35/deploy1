from django.shortcuts import render
from .models import Destination
# Create your views here.

dest1 = Destination()
dest1.name = "Mumbai"
dest1.price = 455
dest1.desc = "Capital of Mahareshtra"
dest1.img = 'destination_1.jpg'
dest1.offer = False

dest2 = Destination()
dest2.name = "Delhi"
dest2.price = 750
dest2.desc = "Capital of India"
dest2.img = ''
dest2.offer = True

dest3 = Destination()
dest3.name = "Benluru"
dest3.price = 455
dest3.desc = "Capital of Karnataka"
dest3.img = 'destination_1.jpg'
dest3.offer = False

dests = [dest1, dest2, dest3]

def index(request):
    return render(request, 'index.html',{'dests': dests} )
