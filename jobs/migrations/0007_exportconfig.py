# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import jobs.models
import uuid

def get_upload_path(instance, filename):
    """
    Construct the path to where the uploaded config file is to be stored.
    """
    configtype = instance.config_type.lower()
    # sanitize the filename here..
    path = 'export/config/{0}/{1}'.format(configtype, instance.filename)
    return path

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_job_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportConfig',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(default='PRESET', max_length=10, choices=[('PRESET', 'Preset'), ('TRANSLATION', 'Translation'), ('TRANSFORM', 'Transform')])),
                ('filename', models.CharField(max_length=255)),
                ('upload', models.FileField(max_length=255, upload_to=get_upload_path)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
