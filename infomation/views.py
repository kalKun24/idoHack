from django.shortcuts import render
from django.views.generic import ListView
from .models import Infomation


class Index(ListView):
    template_name = 'infomation/index.html'
    model = Infomation
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['infomation_list'] =Infomation.objects.all().order_by('-updated_at')
        return context
