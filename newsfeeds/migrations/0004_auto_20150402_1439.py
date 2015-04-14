# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0003_auto_20150402_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.DateTimeField(verbose_name=b'date of news'),
            preserve_default=True,
        ),
    ]
