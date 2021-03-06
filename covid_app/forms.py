from django import forms
from .models import Event, Person, Scanner, Location


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('initiator', 'location')


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class ScannerForm(forms.ModelForm):

    class Meta:
        model = Scanner
        fields = ('barcode',)

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('location',)