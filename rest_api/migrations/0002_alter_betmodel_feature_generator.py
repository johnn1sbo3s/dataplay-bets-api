# Generated by Django 5.2.3 on 2025-07-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betmodel',
            name='feature_generator',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
