# Generated by Django 3.1.7 on 2021-04-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_chat', '0010_auto_20210427_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversations',
            name='text',
            field=models.TextField(max_length=575),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=1450),
        ),
    ]
