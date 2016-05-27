# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 14:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):

    replaces = [('annotations', '0001_initial'), ('annotations', '0002_auto_20160524_0306'), ('annotations', '0003_auto_20160527_1450')]

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manifestos', '0008_auto_20160503_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', models.TextField(blank=True)),
                ('text_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manifestos.Manifesto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('annotator_schema_version', models.CharField(blank=True, max_length=8)),
                ('quote', models.TextField(default='')),
                ('range_end', models.CharField(blank=True, max_length=50)),
                ('range_end_offset', models.BigIntegerField(default=0)),
                ('range_start', models.CharField(blank=True, max_length=50)),
                ('range_start_offset', models.BigIntegerField(default=0)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('uri', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]