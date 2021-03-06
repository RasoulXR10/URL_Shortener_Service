# Generated by Django 3.0.7 on 2020-06-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_auto_20200617_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlappshortener',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='urlappshortener',
            name='shortener',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
