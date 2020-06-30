from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import URLAppShortener


def homeFBV(request, shortener=None, *args, **kwargs):  # Function Based View --> FBV
    obj = get_object_or_404(URLAppShortener, shortener=shortener)
    context = {
        'obj': obj,
    }
    return HttpResponseRedirect(obj.url)


class homeCBV(View):  # Class Based View --> CBV
    def get(self, request, shortener=None, *args, **kwargs):
        obj = get_object_or_404(URLAppShortener, shortener=shortener)
        return HttpResponseRedirect(obj.url)

    # in class based views we should explicitly write the method you want to handle
    def post(self, request, *args, **kwargs):
        return HttpResponse()


'''
    obj = URLAppShortener.objects.get(shortener=shortener)

    try:
        obj = URLAppShortener.objects.get(shortener=shortener)
    except:
        obj = URLAppShortener.objects.all().first()

    obj_url = None
    qs = URLAppShortener.objects.filter(shortener__iexact=shortener.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url

'''
