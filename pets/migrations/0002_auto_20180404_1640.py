# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pets',
            new_name='Pet',
        ),
    ]
