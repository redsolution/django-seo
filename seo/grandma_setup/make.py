import os
from grandma.make import BaseMake
from grandma.models import GrandmaSettings
from seo.grandma_setup.models import SeoSettings

class Make(BaseMake):
    def postmake(self):
        super(Make, self).postmake()
        seo_settings = SeoSettings.objects.get_settings()
        grandma_settings = GrandmaSettings.objects.get_settings()
        grandma_settings.render_to('settings.py', 'seo/grandma/settings.py', {
            'seo_settings': seo_settings,
        })
