from django.contrib import admin
from .models import App
# from .models import App, AppTag


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'tags')
    # search_fields = ('name', 'tags')
    list_per_page = 20


admin.site.register(App, AppAdmin)
# admin.site.register(AppTag)
