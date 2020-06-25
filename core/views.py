from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
from django.views.generic import View, ListView, DetailView, TemplateView


# ---------------------------------------------------------------------------- #
class HomePageView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, 'home.html', context, status=200)
