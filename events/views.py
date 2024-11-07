from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, RSVP, Category
from .forms import EventForm
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def create_event(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', { 'form' : form, 'categories' : categories })

@login_required(login_url='/accounts/login/')
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required(login_url='/accounts/login/')
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'events/delete_event.html', {'event': event})

@login_required(login_url='/accounts/login/')
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        RSVP.objects.create(event=event, attendee=request.user)
        return redirect('event_detail', event_id=event.id)
    return render(request, 'events/rsvp_event.html', {'event': event})

@login_required(login_url='/accounts/login/')
def send_notification(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        attendees = event.rsvps.all()
        recipient_list = [attendee.attendee.email for attendee in attendees]
        send_mail(subject, message, 'your_email@example.com', recipient_list)
        return redirect('event_detail', event_id=event.id)
    return render(request, 'events/send_notification.html', {'event': event})


@login_required(login_url='/accounts/login/')
def search_events(request):
    query = request.GET.get('q')
    events = Event.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'events/search_events.html', {'events': events, 'query': query})

@login_required(login_url='/accounts/login/')
def filter_events(request):
    category = request.GET.get('category')
    date_range = request.GET.get('date_range')
    events = Event.objects.all()
    if category:
        events = events.filter(category__name=category)
    if date_range:
        start_date, end_date = date_range.split(' - ')
        events = events.filter(date__range=[start_date, end_date])
    return render(request, 'events/filter_events.html', {'events': events})


@login_required(login_url='/accounts/login/')
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

