# Generated by Django 5.0.1 on 2024-02-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_usersmodel_options_alter_usersmodel_contactno'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmodel',
            name='Image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
