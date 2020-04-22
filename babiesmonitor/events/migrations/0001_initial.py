# Generated by Django 3.0.5 on 2020-04-22 22:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=80, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=500)),
                ('baby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='babies.Baby')),
            ],
        ),
    ]
