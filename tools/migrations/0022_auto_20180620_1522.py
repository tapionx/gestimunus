# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0021_auto_20180620_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashmovements',
            name='sign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.Operator', verbose_name=b'Sign'),
        ),
    ]