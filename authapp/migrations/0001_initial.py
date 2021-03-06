# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-27 17:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(blank=True, upload_to='pizzashop_log')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coffeeshop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
