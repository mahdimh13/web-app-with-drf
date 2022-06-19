# Generated by Django 4.0.5 on 2022-06-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.TextField()),
                ('time', models.TimeField(default='19:01:24:15')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('value', models.TextField()),
                ('time', models.TimeField(default='19:01:24:15')),
            ],
        ),
    ]
