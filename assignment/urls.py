from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from main import views as main_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'assignment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cleaners/', include('cleaners.urls', namespace='cleaners')),
    url(r'^customers/', include('customers.urls', namespace='customers')),
    url(r'^$', main_views.home, name='home'),
    url(r'^booking/', include('bookings.urls', namespace='booking')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
