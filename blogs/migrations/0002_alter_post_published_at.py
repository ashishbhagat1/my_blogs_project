# Generated by Django 3.2 on 2021-04-21 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(verbose_name=datetime.date(2021, 4, 22)),
        ),
    ]