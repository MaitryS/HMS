# Generated by Django 5.0.1 on 2024-02-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_roomtypemodel_remove_staffmodel_image_usersmodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersmodel',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='ContactNo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
