# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0034_auto_20180703_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='upload',
            field=models.FileField(null=True, upload_to=b'uploads/2018/07/11/'),
        ),
    ]