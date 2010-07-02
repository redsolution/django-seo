# -*- coding: utf-8 -*-

from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.template.loader import render_to_string
from seo.models import Seo

INTENTS = ['title', 'keywords', 'description', ]

register = template.Library()

class ShowSeo(template.Node):
    def __init__(self, intent, object):
        self.intent = intent
        self.object = object

    def render(self, context):
        object = template.Variable(self.object).resolve(context)
        try:
            seo = Seo.objects.get(
                content_type=ContentType.objects.get_for_model(
                        object.__class__),
                object_id=object.id)
        except ObjectDoesNotExist:
            seo = Seo()
        return render_to_string('seo/%s.html' % self.intent, {
            'seo': seo,
        }, context_instance=template.RequestContext(context.get('request', HttpRequest())))


def show_seo(parser, token):
    """Show seo data for object"""
    splited = token.split_contents()
    if len(splited) != 4 or splited[1] not in INTENTS or splited[2] != 'for':
        raise template.TemplateSyntaxError, "Invalid syntax. Use ``{% show_seo <title|keywords|description> for <object> %}``"
    return ShowSeo(splited[1], splited[3])

register.tag('show_seo', show_seo)


class GetSeo(template.Node):
    def __init__(self, intent, object, variable):
        self.intent = intent
        self.object = object
        self.variable = variable

    def render(self, context):
        object = template.Variable(self.object).resolve(context)
        try:
            seo = Seo.objects.get(
                content_type=ContentType.objects.get_for_model(
                        object.__class__),
                object_id=object.id)
        except ObjectDoesNotExist:
            seo = Seo()
        context[self.variable] = getattr(seo, self.intent)
        return u''

def get_seo(parser, token):
    """Show seo data for object"""
    splited = token.split_contents()
    if len(splited) != 6 or splited[1] not in INTENTS or splited[2] != 'for' or splited[4] != 'as':
        raise template.TemplateSyntaxError, "Invalid syntax. Use ``{% get_seo <title|keywords|description> for <object> as <variable> %}``"
    return GetSeo(splited[1], splited[3], splited[5])

register.tag('get_seo', get_seo)
