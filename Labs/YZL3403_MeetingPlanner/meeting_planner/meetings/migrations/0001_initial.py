# Generated by Django 5.0.1 on 2024-01-07 09:22

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=20)),
                ('room_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('duration', models.IntegerField(default=1)),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.rooms')),
            ],
            options={
                'verbose_name_plural': 'meetings',
            },
        ),
    ]