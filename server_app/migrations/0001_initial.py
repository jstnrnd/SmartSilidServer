# Generated by Django 5.0.7 on 2024-08-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerLogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('computerName', models.CharField(max_length=255)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('middleName', models.CharField(max_length=255)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
    ]
