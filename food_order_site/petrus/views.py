from django.shortcuts import render
from petrus.models import reservation_form
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def index(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            table = reservation_form()
            table.name = request.POST.get('name')
            table.email = request.POST.get('email')
            table.occasion = request.POST.get('occasion')
            table.date_and_time = request.POST.get('date')
            table.message = request.POST.get('message')
            table.save()
            messages.success(request, 'Record saved successfully')
        return render(request, 'index.html')
    return render(request, 'index.html')
