from django.shortcuts import render

from .models import Worker
from django.views.generic import ListView

class WorkerView(ListView):
    model=Worker
    context_object_name="work"
    template_name="index.html"
