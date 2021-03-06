# Generated by Django 4.0.4 on 2022-05-12 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0003_room_description_alter_hotel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('cost', models.FloatField(default=0, max_length=50)),
                ('available', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels.hotel')),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
