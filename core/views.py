from django.views.generic import ListView
from django.shortcuts import render
from .models import Usuario

# Create your views here.

class index(ListView):
    model = Usuario
    template_name = 'core/index.html'
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        return context
