from django.contrib import admin
# from .models import Project, Tag
from .models import Example, ExampleTag


class ExampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'exampletags')
    list_per_page = 20


admin.site.register(Example, ExampleAdmin)
admin.site.register(ExampleTag)

