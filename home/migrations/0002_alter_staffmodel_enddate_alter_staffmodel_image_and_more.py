# Generated by Django 5.0.1 on 2024-02-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmodel',
            name='Enddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='Image',
            field=models.ImageField(null=True, upload_to='home/StaffImg'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='Startdate',
            field=models.DateTimeField(null=True),
        ),
    ]