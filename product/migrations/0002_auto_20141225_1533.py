# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_image'),
        ('cms', '0007_auto_20141028_1559'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.FloatField(default=0.0, verbose_name='price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('url', models.URLField(default=b'http://yuelingshan.com/', verbose_name='url')),
                ('images', models.ManyToManyField(to='filer.Image')),
            ],
            options={
                'ordering': ['-updated'],
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default=b'Product Gallery Title', max_length=255, verbose_name='title')),
                ('description', models.TextField(default=b'Product Gallery Sub-Title.', verbose_name='description')),
                ('count', models.IntegerField(default=4, verbose_name='count')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='watch',
            name='images',
        ),
        migrations.DeleteModel(
            name='Watch',
        ),
    ]
