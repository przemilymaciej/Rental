# Generated by Django 3.2 on 2021-05-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('author', 'title', 'genre')},
        ),
        migrations.AlterUniqueTogether(
            name='cd',
            unique_together={('genre', 'tracks')},
        ),
        migrations.AlterUniqueTogether(
            name='film',
            unique_together={('director', 'title', 'length')},
        ),
    ]
