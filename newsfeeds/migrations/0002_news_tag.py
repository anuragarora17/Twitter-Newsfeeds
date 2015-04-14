# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
=======
import datetime
from django.utils.timezone import utc
>>>>>>> 6a7c6ab5b354e357ecf798dc5f99cb2e4ec09e4d


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tag',
<<<<<<< HEAD
            field=models.CharField(default='#tag', max_length=100),
=======
            field=models.CharField(default=datetime.datetime(2015, 3, 26, 18, 52, 58, 625949, tzinfo=utc), max_length=100),
>>>>>>> 6a7c6ab5b354e357ecf798dc5f99cb2e4ec09e4d
            preserve_default=False,
        ),
    ]
