# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-27 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_tea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.Coffee')),
            ],
        ),
        migrations.AlterField(
            model_name='tea',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tea',
            name='type_choice',
            field=models.CharField(choices=[('Черный', 'Черный'), ('Зеленый', 'Зеленый'), ('Фруктовый', 'Фруктовый')], max_length=30),
        ),
    ]