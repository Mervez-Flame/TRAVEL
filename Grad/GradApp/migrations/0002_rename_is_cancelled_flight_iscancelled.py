# Generated by Django 4.2.1 on 2023-08-29 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GradApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='is_cancelled',
            new_name='iscancelled',
        ),
    ]