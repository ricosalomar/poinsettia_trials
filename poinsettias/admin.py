from django.contrib import admin
from poinsettias.models import *

class RegionAdmin(admin.ModelAdmin):
    fields = ['region']

class BreederAdmin(admin.ModelAdmin):
    fields = ['breeder']

class VarietyAdmin(admin.ModelAdmin):
    fields = ['variety', 'region', 'color', 'vigor', 'timing', 'breeder', 'summary']

class TrialAdmin(admin.ModelAdmin):
    fields = ['year', 'variety', 'bracht_color', 'antithesis', 'height', 'bracht_diameter']

class ImageAdmin(admin.ModelAdmin):
    fields = ['url', 'alt_text']

admin.site.register(Breeder, BreederAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Trial, TrialAdmin)
