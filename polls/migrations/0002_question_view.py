# Generated by Django 2.2.4 on 2020-03-31 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
