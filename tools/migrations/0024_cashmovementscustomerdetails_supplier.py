# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0023_auto_20180622_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashmovementscustomerdetails',
            name='supplier',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Supplier'),
        ),
    ]
