# Generated by Django 5.0.2 on 2024-02-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barapp', '0018_login_action_proreg_action_alter_proreg_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
