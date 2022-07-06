from django.contrib import admin


class NameFilter(admin.SimpleListFilter):
    title = 'Name initial'
    parameter_name = 'initial'

    def lookups(self, request, model_admin):
        return (
            ('b', "Starts with 'b'"),
            ('p', "Starts with 'p'")
        )

    def queryset(self, request, queryset):
        if self.value() == 'b':
            return queryset.filter(name__istartswith='b')
        if self.value() == 'p':
            return queryset.filter(name__istartswith='p')
