# Generated by Django 4.0 on 2023-12-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='cleared_counts',
            field=models.IntegerField(default=0),
        ),
    ]