# Generated by Django 4.0.3 on 2022-03-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_users',
            name='Username',
            field=models.CharField(default='abc', max_length=20),
            preserve_default=False,
        ),
    ]
