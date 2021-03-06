# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-20 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_packing_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw',
            name='factory_wise_bifercation',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='hsn_code',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='material_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='material_type',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='purchase_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='supplier_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='transpoter',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
