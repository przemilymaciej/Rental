# Generated by Django 3.2 on 2021-05-26 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0017_auto_20210526_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 42, 8, 991662)),
        ),
        migrations.AlterField(
            model_name='cdrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 42, 8, 994653)),
        ),
        migrations.AlterField(
            model_name='filmrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 42, 8, 993655)),
        ),
    ]
