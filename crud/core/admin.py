from django.contrib import admin
from .models import CrudModel
# Register your models here.

@admin.register(CrudModel)
class CrudModelAdmin(admin.ModelAdmin):
    list_display=['id','name','heroic_name']


# admin.site.register(CrudModel)