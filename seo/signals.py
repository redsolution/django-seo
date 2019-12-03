from django.db.models.signals import post_save, post_delete
from .models import Seo
from django.core.cache import cache


def seo_changed_handler(sender, instance, **kwargs):
    cache.delete('seo-%d-%d' % (instance.content_type.id, instance.object_id))

post_save.connect(seo_changed_handler, Seo)
post_delete.connect(seo_changed_handler, Seo)