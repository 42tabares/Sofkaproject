# Generated by Django 4.0.4 on 2022-05-15 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0024_alter_reservation_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 14, 20, 47, 33, 894393)),
        ),
    ]
