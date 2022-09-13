# Generated by Django 4.1 on 2022-09-13 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, help_text='날짜', null=True)),
                ('point', models.IntegerField(blank=True, help_text='포인트', null=True)),
                ('garbage', models.FloatField(blank=True, help_text='쓰레기양', null=True)),
                ('path', models.ForeignKey(blank=True, help_text='경로', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='path', to='map.path')),
            ],
        ),
    ]
