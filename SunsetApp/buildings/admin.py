from django.contrib import admin
from buildings.models import *

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'get_image',
                    'owner',
                    'city',
                    'created', )

    list_display_links = ('name',)
    list_filter = ('city',)
