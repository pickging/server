# Generated by Django 4.1 on 2022-09-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='km',
            field=models.FloatField(default=0, help_text='km'),
        ),
    ]
