# Generated by Django 5.0.1 on 2024-02-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbooking',
            name='date',
            field=models.DateField(),
        ),
    ]