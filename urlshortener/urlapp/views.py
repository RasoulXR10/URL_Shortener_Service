from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def homeFBV(request, *args, **kwargs):  # Function Based View --> FBV
    return render(request, 'urlapp/home.html', {})


class homeCBV(View):  # Class Based View --> CBV
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Bitches!</h1>")
