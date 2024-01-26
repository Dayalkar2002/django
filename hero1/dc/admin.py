from django.contrib import admin
from dc.models import Dc
# Register your models here.

@admin.register(Dc)
class DcAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name','city']



# admin.site.register(Dc)