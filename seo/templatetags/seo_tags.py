# -*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ImproperlyConfigured
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from seo.models import Seo, Url

INTENTS = ['title', 'keywords', 'description', ]

register = template.Library()

class SeoNode(template.Node):
    def __init__(self, intent, object, variable):
        self.intent = intent
        self.object = object
        self.variable = variable

    def render(self, context):
        if self.object is None:
            object = None
        else:
            object = template.Variable(self.object).resolve(context)
        try:
            if object is None:
                raise ObjectDoesNotExist
            seo = Seo.objects.get(
                content_type=ContentType.objects.get_for_model(
                        object.__class__),
                object_id=object.id)
        except ObjectDoesNotExist:
            try:
                request = context['request']
            except KeyError:
                raise ImproperlyConfigured('`request` was not found in context. Add "django.core.context_processors.request" to `TEMPLATE_CONTEXT_PROCESSORS` in your settings.py.')
            try:
                object = Url.objects.get(url=request.path_info)
                seo = Seo.objects.get(
                    content_type=ContentType.objects.get_for_model(
                            object.__class__),
                    object_id=object.id)
            except ObjectDoesNotExist:
                seo = Seo()
        if self.variable is None:
            return escape(getattr(seo, self.intent))
        else:
            context[self.variable] = getattr(seo, self.intent)
            return u''

def seo_tag(parser, token):
    """Get seo data for object"""
    splited = token.split_contents()
    if splited[1] in INTENTS:
        if len(splited) in [4, 6] and splited[2] == 'for':
            if len(splited) == 4:
                return SeoNode(splited[1], splited[3], None)
            elif splited[4] == 'as':
                return SeoNode(splited[1], splited[3], splited[5])
        elif len(splited) in [2, 4]:
            if len(splited) == 2:
                return SeoNode(splited[1], None, None)
            elif splited[2] == 'as':
                return SeoNode(splited[1], None, splited[3])
    raise template.TemplateSyntaxError, "Invalid syntax. Use ``{% seo <title|keywords|description> [for <object>] [as <variable>] %}``"
register.tag('seo', seo_tag)
