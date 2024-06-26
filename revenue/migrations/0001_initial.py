# Generated by Django 5.0.4 on 2024-05-07 03:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankingAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NetRevenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RevenueValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField()),
                ('details', models.CharField(blank=True, max_length=250, null=True)),
                ('fixed_revenue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revenue.bankingassociation')),
            ],
        ),
    ]
