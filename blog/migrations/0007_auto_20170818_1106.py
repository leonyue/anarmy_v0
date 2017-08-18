# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 03:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_userextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextra',
            name='boundUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to=settings.AUTH_USER_MODEL),
        ),
    ]
