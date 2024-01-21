# Generated by Django 5.0.1 on 2024-01-20 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Modified', 'Modified'), ('Passive', 'Passive')], default='Active', max_length=10)),
                ('ip_address', models.CharField(default='DESKTOP-77MU1AM', max_length=50)),
                ('machine_name', models.CharField(default='25.30.9.54', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('brand', models.CharField(default='un-brand', max_length=250)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Modified', 'Modified'), ('Passive', 'Passive')], default='Active', max_length=10)),
                ('ip_address', models.CharField(default='DESKTOP-77MU1AM', max_length=50)),
                ('machine_name', models.CharField(default='25.30.9.54', max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]