from django.contrib import admin
from .models import Danhsach_CoTruong
# Register your models here.

class DanhsachAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Specialized']
    list_filter = ['Level']
    search_fields = ['Level']
admin.site.register(Danhsach_CoTruong, DanhsachAdmin)
