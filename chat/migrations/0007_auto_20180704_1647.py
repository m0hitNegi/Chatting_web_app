# Generated by Django 2.0 on 2018-07-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_user_is_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=' ', max_length=70),
        ),
    ]
