# Generated by Django 5.0.1 on 2024-02-10 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='FeedbackId',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='Staff_ID',
        ),
    ]
