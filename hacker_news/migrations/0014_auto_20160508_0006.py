# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0013_auto_20160507_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hacker_news.Comment'),
        ),
    ]
