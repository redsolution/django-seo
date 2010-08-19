# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.core.exceptions import ImproperlyConfigured
from seo.importpath import importpath
from seo.forms import SeoForm
from seo.models import Seo, Url

class SeoInlines(generic.GenericStackedInline):
    model = Seo
    form = SeoForm
    extra = 1
    max_num = 1

class SeoAdmin(admin.ModelAdmin):
    model = Seo

try:
    admin.site.register(Seo, SeoAdmin)
except admin.sites.AlreadyRegistered:
    pass

class UrlAdmin(admin.ModelAdmin):
    model = Url
    inlines = [SeoInlines]

try:
    admin.site.register(Url, UrlAdmin)
except admin.sites.AlreadyRegistered:
    pass

if not hasattr(settings, 'SEO_FOR_MODELS'):
    raise ImproperlyConfigured('Please add ``SEO_FOR_MODELS = ["<app>.admin.<ModelAdmin>",]`` to your settings.py')

for model_name in settings.SEO_FOR_MODELS:
    model = importpath(model_name, 'SEO_FOR_MODELS')
    try:
        model_admin = admin.site._registry[model].__class__
    except KeyError:
        raise ImproperlyConfigured('Please set ``seo`` in your settings.py only as last INSTALLED_APPS')
    admin.site.unregister(model)

    setattr(model_admin, 'inlines', getattr(model_admin, 'inlines', []))
    if not SeoInlines in model_admin.inlines:
        model_admin.inlines = list(model_admin.inlines)[:] + [SeoInlines]

    admin.site.register(model, model_admin)
