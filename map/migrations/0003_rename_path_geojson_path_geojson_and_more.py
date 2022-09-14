# Generated by Django 4.1 on 2022-09-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_remove_path_path_coordinate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='path',
            old_name='path_geojson',
            new_name='geojson',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='path_length',
            new_name='length',
        ),
        migrations.RenameField(
            model_name='spot',
            old_name='spot_geojson',
            new_name='geojson',
        ),
        migrations.RenameField(
            model_name='spot',
            old_name='spot_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='path',
            name='name',
            field=models.CharField(default='pathname', help_text='경로 이름', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='name',
            field=models.CharField(default='path', help_text='스팟 이름', max_length=15),
            preserve_default=False,
        ),
    ]
