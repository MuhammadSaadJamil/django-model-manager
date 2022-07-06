from django.shortcuts import render
from django.views.generic import ListView

from .models import Object


class ListObjects(ListView):
    template_name = 'list.html'
    context_object_name = "items"

    def get_queryset(self, *args, **kwargs):
        # qs = Object.objects.filter(quantity__gte=10)
        qs = Object.manager.quantity_gte(20)
        return qs
