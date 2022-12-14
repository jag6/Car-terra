# Generated by Django 4.1.3 on 2022-11-28 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='body_style',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='make',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
