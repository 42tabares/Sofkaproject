# Generated by Django 4.0.4 on 2022-05-15 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0023_rename_user_id_reservation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 14, 20, 47, 25, 160797)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(default='1', max_length=1),
        ),
    ]