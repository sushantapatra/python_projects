# Generated by Django 4.2.6 on 2023-10-21 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 21, 20, 40, 45, 728801)),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 21, 20, 40, 45, 728801)),
        ),
    ]
