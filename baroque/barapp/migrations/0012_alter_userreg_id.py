# Generated by Django 5.0.2 on 2024-02-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0011_rename_provfeedback_userfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='id',
            field=models.IntegerField(primary_key=1, serialize=False),
        ),
    ]