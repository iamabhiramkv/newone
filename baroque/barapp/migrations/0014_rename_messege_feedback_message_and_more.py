# Generated by Django 5.0.2 on 2024-02-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0013_alter_feedback_id_alter_proreg_id_alter_tbooking_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='messege',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='userfeedback',
            old_name='messege',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='proreg',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tbooking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
