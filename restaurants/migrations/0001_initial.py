# Generated by Django 3.2.13 on 2022-11-03 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('shop_number', models.CharField(max_length=80)),
                ('between_pay', models.CharField(max_length=80)),
                ('opening_time', models.CharField(max_length=80)),
                ('break_day', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag1', models.CharField(blank=True, max_length=20)),
                ('tag2', models.CharField(blank=True, max_length=20)),
                ('tag3', models.CharField(blank=True, max_length=20)),
                ('tag4', models.CharField(blank=True, max_length=20)),
                ('tag5', models.CharField(blank=True, max_length=20)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
