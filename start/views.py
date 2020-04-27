from django.shortcuts import render, get_object_or_404
from start.models import Coffee, Tea

# Create your views here.

def home(request):
    coffee = Coffee.objects.all()
    tea = Tea.objects.all()
    cnt ={
        'coffee': coffee,
        'tea': tea
    }
    return render(request, 'index.html', cnt)


def coffee(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)

    return render(request, 'coffee.html', {'coffee': coffee})
