# Generated by Django 2.1.4 on 2018-12-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colors',
            name='hex_color',
        ),
        migrations.AddField(
            model_name='colors',
            name='color',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='colors',
            name='hexa',
            field=models.TextField(default='', max_length=10),
        ),
    ]