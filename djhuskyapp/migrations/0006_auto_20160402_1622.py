# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djhuskyapp', '0005_auto_20160402_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ('name',)},
        ),
    ]
