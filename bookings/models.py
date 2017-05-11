from django.db import models

from customers.models import Customer
from cleaners.models import Cleaner


class Booking(models.Model):
    customer = models.ForeignKey(Customer, related_name='booking')
    cleaner = models.ForeignKey(Cleaner, related_name='booking')
    date = models.DateTimeField()
