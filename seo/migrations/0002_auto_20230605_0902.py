# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='description',
            field=models.CharField(default=b'', max_length=1000, verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seo',
            name='title',
            field=models.CharField(default=b'', max_length=1000, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
    ]
