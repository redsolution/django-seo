# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200, verbose_name='Title', blank=True)),
                ('description', models.CharField(default=b'', max_length=200, verbose_name='Description', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=1000, verbose_name='Keywords', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'SEO fields',
                'verbose_name_plural': 'SEO fields',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'/', help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", unique=True, max_length=200, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='seo',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
