# Generated by Django 5.0.1 on 2024-01-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0005_proreg_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phn_no', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('no_of_people', models.IntegerField()),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
    ]
