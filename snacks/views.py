# from django.shortcuts import render
#
# # Create your views here.
from django.views.generic import TemplateView


# configure the view
class HomePageView(TemplateView):
    template_name = 'home.html'
