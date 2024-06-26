# Generated by Django 5.0.4 on 2024-05-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_category_alter_expense_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
