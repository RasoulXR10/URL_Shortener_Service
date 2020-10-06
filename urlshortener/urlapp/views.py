from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import URLAppShortener


def home_view_fbv(request, *args, **kargs):
    if request.method == "POST":
        print(request.POST)

    return render(request, "urlapp/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kargs):
        return render(request, "urlapp/home.html", {})

    def post(self, request, *args, **kargs):
        print(request.POST)
        return render(request, "urlapp/home.html", {})


class homeCBV(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(URLAppShortener, shortener=shortcode)
        return HttpResponse("hello again {sc}").format(sc=shortcode)

    # in class based views we should explicitly write the method you want to handle
    # def post(self, request, *args, **kwargs):
    #     return HttpResponse()
