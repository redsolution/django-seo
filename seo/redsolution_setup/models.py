# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from redsolutioncms.models import BaseSettings

class SeoSettings(BaseSettings):
    pass

class SeoModel(models.Model):
    settings = models.ForeignKey(SeoSettings, related_name='models')
    model = models.CharField(verbose_name=_('Mode'), max_length=255)
