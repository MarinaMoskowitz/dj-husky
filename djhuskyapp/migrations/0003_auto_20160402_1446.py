# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djhuskyapp', '0002_auto_20160402_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='id',
            new_name='party_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='id',
            new_name='song_id',
        ),
    ]
