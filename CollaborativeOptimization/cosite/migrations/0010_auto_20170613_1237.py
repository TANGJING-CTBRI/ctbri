# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 04:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosite', '0009_auto_20170602_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpumemory',
            name='add_time',
            field=models.CharField(default='-1', help_text='添加时间', max_length=100),
        ),
        migrations.AlterField(
            model_name='testcasestate',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 13, 12, 37, 57, 520586), help_text='添加时间'),
        ),
    ]
