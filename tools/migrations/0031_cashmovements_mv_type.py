# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0025_movementstype'),
        ('tools', '0030_auto_20180627_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashmovements',
            name='mv_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.MovementsType', verbose_name=b'Type'),
        ),
    ]
