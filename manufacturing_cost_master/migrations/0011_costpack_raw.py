# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_packing_master', '0001_initial'),
        ('manufacturing_cost_master', '0010_auto_20180222_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='costpack',
            name='Raw',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='raw_packing_master.raw'),
            preserve_default=False,
        ),
    ]
