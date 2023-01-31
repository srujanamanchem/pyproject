from django.contrib import admin
from .models import prdanalysis
# Register your models here.

class Production(admin.ModelAdmin):
    list_display = ('id','es_target', 'ac_target', 'bonus', 'score', 'date', 'time')

admin.site.register(prdanalysis, Production)
