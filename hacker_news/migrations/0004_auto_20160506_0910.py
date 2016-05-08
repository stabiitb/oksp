# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0003_auto_20160506_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('comments', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]