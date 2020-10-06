
from django.contrib import admin
from django.urls import path, re_path
from urlapp.views import HomeView, homeCBV
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='homeFBV'),
    url(r'^(?P<shortcode>[\w-]+)/$', homeCBV.as_view(), name='homeCBV'),
]
