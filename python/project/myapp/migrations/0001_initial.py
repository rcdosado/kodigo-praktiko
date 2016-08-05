# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Development'), ('2', 'Implementation'), ('3', 'Unknown')], default=3, max_length=1)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamlead', to='myapp.Person')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(blank=True, help_text='Create/Select a team for this project', related_name='ProjectTeam', to='myapp.Team'),
        ),
    ]