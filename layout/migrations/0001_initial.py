# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-14 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdjMat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat', models.TextField(verbose_name='Node邻接矩阵')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '邻接矩阵',
                'verbose_name': '邻接矩阵',
            },
        ),
        migrations.CreateModel(
            name='EQLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(default='', max_length=50, verbose_name='机台名称')),
                ('unit', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='机台子单元名称')),
                ('floor', models.CharField(choices=[('L20', 'L20'), ('L40', 'L40')], default='楼层未选', max_length=10, verbose_name='楼层')),
                ('vertex', models.CharField(max_length=500, verbose_name='顶点坐标')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '机台外框图',
                'verbose_name': '机台外框图',
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('nodeNo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Node No')),
                ('floor', models.CharField(choices=[('L20', 'L20'), ('L40', 'L40')], default='楼层未选', max_length=10, verbose_name='楼层')),
                ('x_axis', models.IntegerField(verbose_name='x axis')),
                ('y_axis', models.IntegerField(verbose_name='y axis')),
                ('reach_node', models.CharField(max_length=300, verbose_name='可达节点')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '节点',
                'verbose_name': '节点',
            },
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_floor', models.CharField(choices=[('L10', 'L10'), ('L20', 'L20'), ('L30', 'L30'), ('L40', 'L40')], default='楼层未选', max_length=10, verbose_name='起点楼层')),
                ('start_point', models.CharField(default='', max_length=10, verbose_name='起点坐标')),
                ('end_floor', models.CharField(choices=[('L10', 'L10'), ('L20', 'L20'), ('L30', 'L30'), ('L40', 'L40')], default='楼层未选', max_length=10, verbose_name='终点楼层')),
                ('end_point', models.CharField(default='', max_length=10, verbose_name='终点坐标')),
                ('path_node', models.TextField(blank=True, max_length=2000, null=True, verbose_name='路径节点')),
                ('path_axis', models.TextField(blank=True, max_length=2000, null=True, verbose_name='路径节点坐标')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '路径图',
                'verbose_name': '路径图',
            },
        ),
    ]
