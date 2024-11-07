from django.shortcuts import render
from events.models import Event

def home(request):
    if request.user.is_authenticated:
        events = Event.objects.all()
        return render(request, 'index.html', {'events': events})
    else:
        return render(request, 'index.html')