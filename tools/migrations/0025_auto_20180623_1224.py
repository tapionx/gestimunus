# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0024_cashmovementscustomerdetails_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashmovements',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diary',
            name='upload',
            field=models.FileField(null=True, upload_to=b'uploads/2018/06/23/'),
        ),
    ]
