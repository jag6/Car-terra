# Generated by Django 4.1.3 on 2022-12-19 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0002_alter_inquiry_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='inquiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
