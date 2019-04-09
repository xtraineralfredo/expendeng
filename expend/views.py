from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from expend.models import Source


class SourceList(ListView):
    model = Source

    def get_queryset(self):
        return Source.objects.filter(user=self.request.user)
