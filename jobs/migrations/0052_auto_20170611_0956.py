# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-11 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0051_auto_20170610_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='feature_selection',
            field=models.TextField(validators=[jobs.models.validate_feature_selection]),
        ),
    ]
