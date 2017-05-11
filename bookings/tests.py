from django.core.urlresolvers import reverse_lazy
from django.test import TestCase

from bookings.forms import BookingCreateForm
from bookings.models import Booking
from cities.models import City
from cleaners.models import Cleaner
from customers.models import Customer


class BookingCreateFormTest(TestCase):
    """
    Test booking creation form
    """
    def setUp(self):
        self.city = City.objects.create(name='London')

        self.cleaner = Cleaner.objects.create(
            first_name='Dmitry', last_name='Moroz', quality_score=5
        )
        self.cleaner.cities.add(self.city)

        self.customer = Customer.objects.create(
            first_name='Rod', last_name='Chuba', phone_number='9999999999'
        )

        self.data = {
            'first_name': 'Rod',
            'last_name': 'Chuba',
            'phone_number': '9999999999',
            'city': 1,
            'date': '2000-12-12',
        }

    def test_temlate(self):
        self.assertTemplateUsed('booking/booking_form.html')

    def test_page_code(self):
        url = reverse_lazy('booking:new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_form(self):
        form = BookingCreateForm(data={})
        self.assertFalse(form.is_valid())

        form = BookingCreateForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_form_data_exists(self):
        Booking.objects.create(
            customer=self.customer, cleaner=self.cleaner, date='2000-12-12'
        )
        form = BookingCreateForm(data=self.data)
        self.assertFalse(form.is_valid())
