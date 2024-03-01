from django.contrib import admin
from .models import CrModel
# Register your models here.

@admin.register(CrModel)
class CrModelAdmin(admin.ModelAdmin):
    list_display=['name','heroic_name']

# admin.site.register(CrModel)