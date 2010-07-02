# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Seo(models.Model):
    class Meta:
        verbose_name = _('SEO')
        verbose_name_plural = _('SEO')

    title = models.CharField(verbose_name=_('Title'),
        max_length=200, default='', blank=True)
    description = models.CharField(verbose_name=_('Description'),
        max_length=200, default='', blank=True)
    keywords = models.CharField(verbose_name=_('Keywords'),
        max_length=1000, default='', blank=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title
