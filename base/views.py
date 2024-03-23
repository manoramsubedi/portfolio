from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
#from django.http import HttpResponse

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["about"] =About.objects.first()
        context["services"] =Service.objects.all()
        context["works"] =RecentWork.objects.all()
        return context
    














#vid 6 
# https://www.youtube.com/watch?v=fHzg-9laU88&list=PL_DFzAO9UnFRLw-YGJQCO5BIE2cDyTgFC&index=6&ab_channel=ManjurulHoque
