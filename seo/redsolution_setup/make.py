import os
from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings
from seo.redsolution_setup.models import SeoSettings

class Make(BaseMake):
    def make(self):
        super(Make, self).make()
        seo_settings = SeoSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to(['..', 'templates', 'base_seo.html'],
            'seo/redsolutioncms/base_seo.html', {
            'seo_settings': seo_settings,
        }, 'w')
        cms_settings.base_template = 'base_seo.html'
        cms_settings.save()

    def postmake(self):
        super(Make, self).postmake()
        seo_settings = SeoSettings.objects.get_settings()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'seo/redsolutioncms/settings.pyt', {
            'seo_settings': seo_settings,
        })

make = Make()
