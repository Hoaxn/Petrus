# Generated by Django 4.0.6 on 2022-07-25 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation_form',
            name='date_and_time',
            field=models.CharField(max_length=50),
        ),
    ]
