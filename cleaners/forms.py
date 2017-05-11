from django import forms

from .models import Cleaner
from cities.models import City


class CleanerCreationForm(forms.ModelForm):
    """
    Cleaner creation form
    """
    quality_score = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=0,
        max_value=5
    )
    cities = forms.ModelMultipleChoiceField(
        label='cities',
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Cleaner
        fields = '__all__'

    def clean_email(self):
        """
        We do not need validate because Django do it
        """
        super(CleanerCreationForm, self).clean_email()
