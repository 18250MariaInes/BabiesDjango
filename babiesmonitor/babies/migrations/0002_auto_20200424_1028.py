# Generated by Django 3.0.5 on 2020-04-24 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baby',
            old_name='lastName',
            new_name='lastname',
        ),
    ]
