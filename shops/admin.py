from django.contrib import admin

from .models import Style, Shop

admin.site.register(Style)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'style')

admin.site.register(Shop, ShopAdmin)
