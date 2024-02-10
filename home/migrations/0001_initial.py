# Generated by Django 5.0.1 on 2024-02-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeedbackId', models.IntegerField()),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_ID', models.IntegerField()),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Image', models.ImageField(null=True, upload_to='img')),
                ('Phone', models.CharField(max_length=100, unique=True)),
                ('Address', models.CharField(max_length=100)),
                ('DOB', models.DateTimeField(null=True)),
                ('Gender', models.CharField(max_length=10)),
                ('Position', models.CharField(max_length=20)),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Startdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('Enddate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]