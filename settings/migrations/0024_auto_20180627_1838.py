# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0023_auto_20180627_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='services',
            field=models.ManyToManyField(blank=True, to='settings.CashDesk'),
        ),
    ]
