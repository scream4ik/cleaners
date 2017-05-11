from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.conf import settings

from .forms import BookingCreateForm
from .models import Booking
from customers.models import Customer
from cleaners.models import Cleaner


class BookingCreateView(FormView):
    """
    View for booking creation
    """
    template_name = 'booking/booking_form.html'
    form_class = BookingCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            customer = Customer.objects.get(
                phone_number=form.data['phone_number']
            )
        except Customer.DoesNotExist:
            customer = Customer()
            customer.first_name = form.data['first_name']
            customer.last_name = form.data['last_name']
            customer.phone_number = form.data['phone_number']
            customer.save()

        cleaner = Cleaner.objects.filter(cities=form.data['city'])\
                                 .exclude(booking__date=form.data['date'])\
                                 .first()

        booking = Booking.objects.create(
            customer=customer, cleaner=cleaner, date=form.data['date']
        )

        template = render_to_string(
            'booking/email_notification.txt', {'booking': booking}
        )
        send_mail(
            'New booking',
            template,
            settings.DEFAULT_FROM_EMAIL,
            [cleaner.email]
        )
        return super(BookingCreateView, self).form_valid(form)


class BookingListView(ListView):
    """
    Booking list
    """
    template_name = 'booking/booking_list.html'
    queryset = Booking.objects.order_by('-date')
