from django.contrib import admin
from .models import Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "is_available", "created_on"]
    # fields = ["name", "quantity", "is_available", "display_date"]
    # exclude = ['is_available']
    date_hierarchy = 'display_date'  # Make slicing available based on date
