from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db import models
from django import forms

from .forms import ObjectForm
from .models import Object
from .adminFilters import NameFilter


@admin.action(description="Update availability")
def update_availability(modeladmin, request, queryset):
    for data in queryset:
        data.is_available = not data.is_available
        data.save()


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "is_available", "created_on", "display_date"]
    list_display_links = ["name", "quantity", "is_available", "created_on", "display_date"]
    # fields = ["name", "quantity", "is_available", "display_date"]
    # exclude = ['is_available']
    date_hierarchy = 'display_date'  # Make slicing available based on date
    empty_value_display = 'NaN'  # how empty values will be displayed
    filter_horizontal = ["ingredients"]
    # filter_vertical = ["ingredients"]
    # form = ObjectForm  # override form with your own custom form
    ist_select_related = ['ingredients']
    list_filter = ['is_available', NameFilter, ('display_date', admin.EmptyFieldListFilter)]
    ordering = ('name', '-quantity',)
    search_fields = ['name', 'ingredients__name']
    actions = [update_availability]
    fieldsets = (
        (None, {
            'fields': ("name", "description", "quantity", "is_available")
        }),
        (
            'Advanced options', {
                'classes': ('collapse',),
                'fields': ('display_date', 'ingredients'),
            }
        )
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.TextInput()},
    }

# My Custom Admin
# class MyAdminSite(AdminSite):
#     site_header = 'My Custom administration'
#
#
# admin_site = MyAdminSite(name='myadmin')
# admin_site.register(Object, ObjectAdmin)
