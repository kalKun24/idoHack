# Generated by Django 4.0 on 2023-12-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_challenge_cleared_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='exercise',
            name='explanation_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='exercise',
            name='reference_url',
            field=models.URLField(default=''),
        ),
    ]
