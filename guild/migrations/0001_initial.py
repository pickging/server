# Generated by Django 4.1.1 on 2022-09-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild_name', models.CharField(help_text='길드 이름', max_length=20, unique=True)),
                ('guild_image', models.ImageField(help_text='길드 이미지', upload_to='')),
                ('region', models.CharField(help_text='길드 지역', max_length=10)),
                ('guild_description', models.CharField(help_text='길드 설명', max_length=50)),
                ('member_number', models.IntegerField(default=1, help_text='길드 멤버수')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
