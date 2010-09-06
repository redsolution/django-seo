from django.contrib import admin
from seo.redsolution_setup.models import SeoSettings, SeoModel

class SeoModelInline(admin.TabularInline):
    model = SeoModel

class SeoSettingsForm(admin.ModelAdmin):
    model = SeoSettings
    inlines = [SeoModelInline]

try:
    admin.site.register(SeoSettings, SeoSettingsForm)
except admin.sites.AlreadyRegistered:
    pass
