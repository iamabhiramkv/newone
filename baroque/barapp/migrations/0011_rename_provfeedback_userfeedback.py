# Generated by Django 5.0.1 on 2024-02-10 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0010_provfeedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='provfeedback',
            new_name='userfeedback',
        ),
    ]