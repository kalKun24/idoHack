from django.contrib import admin
from .models import Infomation

class InfomationAdmin(admin.ModelAdmin):
    list_display = ["title", "autohr", "updated_at"]
    list_filter = ["autohr"]
    search_fields = ["title", "autohr"]
    ordering = ["created_at", "updated_at", "autohr"]
    list_per_page = 20

admin.site.register(Infomation, InfomationAdmin)