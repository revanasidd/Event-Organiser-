# Generated by Django 3.2.9 on 2022-01-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Mobile',
            field=models.IntegerField(),
        ),
    ]
