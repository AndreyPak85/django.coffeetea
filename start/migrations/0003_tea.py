# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-26 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20200426_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_choice', models.CharField(choices=[('Черный', 'Черный'), ('Зеленый', 'Зеленый')], max_length=30)),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('brand', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='start.Brand')),
            ],
        ),
    ]
