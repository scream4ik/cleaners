from django.conf.urls import url

from .views import BookingCreateView, BookingListView


urlpatterns = [
    url(r'^new/$', BookingCreateView.as_view(), name='new'),
    url(r'^list/$', BookingListView.as_view(), name='list'),
]
