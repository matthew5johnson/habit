# Generated by Django 2.1.4 on 2018-12-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hex_color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Emotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=50)),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
            ],
        ),
    ]
