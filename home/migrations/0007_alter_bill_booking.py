# Generated by Django 5.0.1 on 2024-03-22 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_search_checkin_alter_search_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='booking',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='home.booking'),
        ),
    ]