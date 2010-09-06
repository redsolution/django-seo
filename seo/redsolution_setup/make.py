import os
from redsolution.make import BaseMake
from redsolution.models import RedsolutionSettings
from seo.redsolution_setup.models import SeoSettings

class Make(BaseMake):
    def postmake(self):
        super(Make, self).postmake()
        seo_settings = SeoSettings.objects.get_settings()
        redsolution_settings = RedsolutionSettings.objects.get_settings()
        redsolution_settings.render_to('settings.py', 'seo/redsolution/settings.pyt', {
            'seo_settings': seo_settings,
        })
