# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-21 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing_cost_master', '0006_cost_mrp_per'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='helo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raw_packing_master.raw'),
        ),
    ]
