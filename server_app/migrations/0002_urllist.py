# Generated by Django 5.0.7 on 2024-08-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('list_type', models.CharField(choices=[('whitelist', 'Whitelist'), ('blacklist', 'Blacklist')], max_length=10)),
            ],
        ),
    ]
