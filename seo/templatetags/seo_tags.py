# -*- coding: utf-8 -*-
import json
from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from seo.models import Seo, Url

register = template.Library()

DEFAULT_SEO_OBJ = {
    "title": "",
    "desc": "",
    "keys": ""
}


def seo_by_url(context):

    """ Возвращает seo-запись по url запроса (если запись привязана к url) """

    path = context['request'].path_info
    url = Url.objects.filter(url=path).first()
    if url:
        url_ct = ContentType.objects.get_for_model(url.__class__)
        seo = Seo.objects.filter(content_type=url_ct, object_id=url.id).first()
        if seo:
            return {
                "title": seo.title,
                "desc": seo.description,
                "keys": seo.keywords,
            }
    return DEFAULT_SEO_OBJ.copy()


def seo_by_content_object(item, item_ct):

    """ Возвращает seo-запись """

    seo = Seo.objects.filter(content_type=item_ct, object_id=item.id).first()
    if seo:
        return {
            "title": seo.title,
            "desc": seo.description,
            "keys": seo.keywords,
        }
    else:
        return DEFAULT_SEO_OBJ.copy()


def modify_seo(seo, **kwargs):

    """ Добавить префикс или установить дефолтное значение метатегам """

    if not seo["title"]:
        seo["title"] = kwargs.get("title_default", '')
    if seo["title"]:
        title_postfix = kwargs.get("title_postfix")
        if title_postfix:
            seo["title"] += title_postfix

    if not seo["desc"]:
        seo["desc"] = kwargs.get("desc_default", '')
    if seo["desc"]:
        desc_postfix = kwargs.get("desc_postfix")
        if desc_postfix:
            seo["desc"] += desc_postfix

    if not seo["keys"]:
        seo["keys"] = kwargs.get("keys_default", '')
    if seo["keys"]:
        keys_postfix = kwargs.get("keys_postfix")
        if keys_postfix:
            seo["keys"] += keys_postfix
    return seo


@register.inclusion_tag('seo/seo.html', takes_context=True)
def seo(context, item=None, **kwargs):
    if item:
        item_ct = ContentType.objects.get_for_model(item)
        item_cache_key = "seo-%d-%d" % (item_ct.id, item.id)
        item_json_data = cache.get(item_cache_key)
        if not item_json_data:
            item_data = seo_by_content_object(item, item_ct)
            cache.set(item_cache_key, json.dumps(item_data, ensure_ascii=False))
        else:
            item_data = json.loads(item_json_data)
    else:
        item_data = seo_by_url(context)
    return modify_seo(item_data, **kwargs)
