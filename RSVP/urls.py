from django.urls import path
from . import views

urlpatterns=[
    path('join/<int:event_id>/',views.join_event,name='join_event'),
    path('cancel/<int:event_id>/',views.cancel_rsvp,name='cancel_rsvp'),
    path('attendees/<int:event_id>',views.attendee_list,name='attendee_list'),
]