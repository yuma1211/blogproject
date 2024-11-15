from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

class TopView(TemplateView):
    template_name='top.html'