# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0004_auto_20140924_1038'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('domid', models.CharField(max_length=50, verbose_name='Name')),
                ('interval', models.IntegerField(default=5000, help_text=b'The amount of time in milliseconds to delay cycling items. If zero carousel will not automatically cycle.')),
                ('show_title', models.BooleanField(default=True, help_text=b'Display image titles, if true.')),
                ('show_caption', models.BooleanField(default=True, help_text=b'Display image captions, if true.')),
                ('width', models.PositiveIntegerField(default=0, help_text=b'Fixed width in pixels for carousel images.', verbose_name='\u5bbd')),
                ('height', models.PositiveIntegerField(default=0, help_text=b'Fixed height in pixels for carousel images.', verbose_name='height')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption_title', models.CharField(max_length=100, null=True, blank=True)),
                ('caption_content', models.TextField(null=True, blank=True)),
                ('url', models.CharField(default=None, max_length=256, blank=True)),
                ('carousel', models.ForeignKey(to='cmsplugin_carousel.Carousel')),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
