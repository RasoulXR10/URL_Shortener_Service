# Generated by Django 3.0.7 on 2020-06-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0003_auto_20200620_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlappshortener',
            name='shortener',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
