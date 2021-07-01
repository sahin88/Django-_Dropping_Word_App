from django.contrib import admin
from .models import Keys



class KeysAdmin(admin.ModelAdmin):

    list_display = ('id', 'keys',)
    list_display_links = ('id', 'keys',)
    search_fields = ('keys',)
    list_per_page = 24

admin.site.register(Keys,KeysAdmin)
