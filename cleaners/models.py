from django.db import models

from cities.models import City


class Cleaner(models.Model):
    """
    Cleaner model
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    quality_score = models.DecimalField(max_digits=5, decimal_places=2)
    cities = models.ManyToManyField(City)
    email = models.EmailField()

    class Meta:
        verbose_name = 'cleaner'
        verbose_name_plural = 'cleaners'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
