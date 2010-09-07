import os
from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from seo.redsolution_setup.models import SeoSettings

class Make(BaseMake):
    def postmake(self):
        super(Make, self).postmake()
        seo_settings = SeoSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'seo/redsolutioncms/settings.pyt', {
            'seo_settings': seo_settings,
        })

make = Make()
