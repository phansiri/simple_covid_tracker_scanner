from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Person, Event, Location, Unit
from cac_parser import PDF417Barcode
from .forms import EventForm, PersonForm


def event_list(request):
    events = Event.objects.all().order_by('-arrived')
    loc = Location.objects.get()
    context = {
        'events': events,
        'loc': loc,
    }
    return render(request, 'covid_app/event_list.html', context)


def scan(request):
    if request.method.lower() == 'post':
        barcode = request.POST.get('scanner')
        loc_pk = request.POST.get('location')

        item = PDF417Barcode(barcode)  # parse cac for vital information
        person: Person = None
        print(item)
        try:
            person = Person.objects.get(edipi=item.edipi)
        except:
            pass

        print('***************************')
        print(item.fname.strip())
        print('***************************')


        if not person:  # person doesn't exist
            person = Person.objects.create(
                rank=item.rank.strip(),
                lname=item.lname.replace(".", "").strip(),
                fname=item.fname.replace(".", "").strip(),
                branch=item.branch.strip(),
                category=item.category.strip(),
                edipi=item.edipi,
            )
        location = Location.objects.get(pk=loc_pk)

        Event.objects.create(initiator=person, location=location, arrived=timezone.now())

        return redirect('event_list')
