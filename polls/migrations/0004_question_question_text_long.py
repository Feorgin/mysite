# Generated by Django 2.2.4 on 2020-04-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200331_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text_long',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]