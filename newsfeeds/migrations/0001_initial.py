# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
                ('country', models.ForeignKey(to='newsfeeds.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
