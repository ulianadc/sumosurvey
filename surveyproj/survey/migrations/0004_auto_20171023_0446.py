# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20171023_0422'),
    ]

    operations = [
        migrations.RenameModel('Answer', 'Response'),
    ]
