# Generated by Django 4.1.3 on 2022-12-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]