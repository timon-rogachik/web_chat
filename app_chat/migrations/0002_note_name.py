# Generated by Django 3.1.7 on 2021-05-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
