from django.contrib import admin
from .models import Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "is_available", "created_on"]
    # fields = ["name", "quantity", "is_available"]
    # exclude = ['is_available']
    date_hierarchy = 'created_on'
