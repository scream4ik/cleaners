from django import forms

from cities.models import City
from cleaners.models import Cleaner


class BookingCreateForm(forms.Form):
    """
    Form for booking creation by customers
    """
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')
    phone_number = forms.CharField(label='phone')
    city = forms.ModelChoiceField(label='city', queryset=City.objects.all())
    date = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(BookingCreateForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    def clean_date(self):
        """
        look for cleaners that work in the specified city that do not have 
        any bookings that conflict with the time specified
        """
        data = self.cleaned_data
        if not Cleaner.objects.filter(cities=data['city']).exclude(booking__date=data['date']).exists():
            raise forms.ValidationError('We haven\'t available cleaners')
        return data['date']
