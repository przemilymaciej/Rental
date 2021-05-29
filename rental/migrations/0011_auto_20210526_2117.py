# Generated by Django 3.2 on 2021-05-26 19:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0010_auto_20210525_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('length', models.DecimalField(decimal_places=2, max_digits=3)),
                ('CD_amount', models.IntegerField(default=0)),
                ('tracks', models.TextField(max_length=300)),
                ('popularity', models.IntegerField(default=0)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rental.filmgenre')),
            ],
        ),
        migrations.CreateModel(
            name='CDGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a CD genre', max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('popularity', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'CDGenres',
            },
        ),
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 17, 30, 610882)),
        ),
        migrations.AlterField(
            model_name='filmrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 17, 30, 611907)),
        ),
        migrations.CreateModel(
            name='CDRentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(auto_now_add=True)),
                ('back_date', models.DateField(default=datetime.datetime(2021, 6, 25, 21, 17, 30, 613900))),
                ('cd', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='rental.cd')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='CDs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]