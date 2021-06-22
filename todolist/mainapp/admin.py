from django.contrib import admin

from .models import Utask, Category

class UtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'achievement', 'date_create', 'date_update',)
    list_display_links = ('title', 'category', 'achievement',)
    search_fields = ('title', 'category', 'achievement',)

admin.site.register(Utask, UtaskAdmin)
admin.site.register(Category)
