from django.contrib import admin

from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal_name", "meal_category", "price", "status")


admin.site.register(MenuItem, MenuItemAdmin)
