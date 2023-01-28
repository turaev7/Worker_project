from django.contrib import admin

# Register your models here.
from .models import Worker
admin.site.register(Worker)
from .models import *
from .models import Organization
from .models import Worker_info
from .models import Relatives

admin.site.register(Organization)
class RelativeInline(admin.TabularInline):
    model= Relatives
    fields = ["role", 'name', 'date', 'addres', 'work']

@admin.register(Worker_info)

class Worker_infoAdmin(admin.ModelAdmin):
    inlines = [RelativeInline, ]
    list_per_page = 10
