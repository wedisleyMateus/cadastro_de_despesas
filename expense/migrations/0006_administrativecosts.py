# Generated by Django 4.2.13 on 2024-06-07 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_rename_user_expenseuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounting', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('consultancy', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('insurance', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('light', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('water', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Internet', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('depreciation', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('amortization', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
            ],
        ),
    ]
