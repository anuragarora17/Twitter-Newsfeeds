# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.CharField(default=datetime.datetime(2015, 3, 26, 18, 52, 58, 625949, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
