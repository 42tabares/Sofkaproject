# Generated by Django 4.0.4 on 2022-05-14 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0012_remove_roomtype_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 14, 8, 30, 0, 738026)),
        ),
    ]
