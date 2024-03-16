# Generated by Django 5.0.2 on 2024-02-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0015_drinksadd_foodsadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodsaddveg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('detail', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='foodsadd',
            new_name='foodsaddnon',
        ),
    ]
