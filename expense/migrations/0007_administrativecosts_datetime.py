# Generated by Django 4.2.13 on 2024-06-07 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0006_administrativecosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativecosts',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
