# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0005_auto_20150402_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
