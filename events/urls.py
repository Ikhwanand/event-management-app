from django.urls import path
from . import views

app_name='events'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('rsvp/<int:event_id>/', views.rsvp_event, name='rsvp_event'),
    path('send_notification/<int:event_id>/', views.send_notification, name='send_notification'),
    path('search/', views.search_events, name='search_events'),
    path('filter/', views.filter_events, name='filter_events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]