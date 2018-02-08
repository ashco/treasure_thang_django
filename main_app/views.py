from django.shortcuts import render
from django.http import HttpResponse
from .models import Treasure

def index(request):
	# return HttpResponse('<h1>Hello Explorers!</h1>')
	treasures = Treasure.objects.all()
	return render(request, 'index.html', { 'treasures': treasures })
	
def show(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'show.html', { 'treasure': treasure })


	
	# starter data, disabled when models was enabled
# class Treasure:
# 	def __init__(self, name, value, material, location):
# 		self.name = name
# 		self.value = value
# 		self.material = material
# 		self.location = location

# treasures = [
# 	Treasure('Gold nugget', 500.00, 'gold', 'Curly\'s Creed, NM'),
# 	Treasure('Fools Gold', 0, 'pyrite', 'Fools Falls, CO'),
# 	Treasure('Coffee Can', 0.25, 'tin', 'Acme, CA'),
# ]