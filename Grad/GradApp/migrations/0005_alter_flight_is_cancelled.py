# Generated by Django 4.2.1 on 2023-08-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradApp', '0004_alter_flight_is_cancelled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
