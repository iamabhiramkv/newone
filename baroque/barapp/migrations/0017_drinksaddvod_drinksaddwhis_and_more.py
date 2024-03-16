# Generated by Django 5.0.2 on 2024-02-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0016_foodsaddveg_rename_foodsadd_foodsaddnon'),
    ]

    operations = [
        migrations.CreateModel(
            name='drinksaddvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=50)),
                ('variant', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='drinksaddwhis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=50)),
                ('variant', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='drinksadd',
            new_name='drinksaddrum',
        ),
    ]