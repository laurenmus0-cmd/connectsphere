from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import RSVP
from django.shortcuts import render

# Create your views here.
#joining members in the event
def join_event(request,event_id):
    event=get_object_or_404(Event,id=event_id)

    RSVP.objects.get_or_create(
        user=request.user,
        event=event
    )
    return redirect('event_detail',event_id=event.id)

#Terminating RSVP
def cancel_rsvp(request, event_id):
    event=get_object_or_404(Event,id=event_id)    

    RSVP.objects.filter(
        user=request.user,
        event=event
    ).delete()

    return redirect('event_detail',event_id=event.id)

#Attendance of the meeting
def attendee_list(request,event_id):
    event=get_object_or_404(Event,id=event_id)

    attendees=RSVP.objects.filter(event=event)
    return render(request,'rsvp.attendees.html',{
        'event':event,
        'attendees':attendees,
        'count':attendees.count()
    })


