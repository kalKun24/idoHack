# Generated by Django 4.0 on 2023-12-26 06:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('challenges', '0005_alter_challenge_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='identifier',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='^[0-9a-zA-Z]*$')], verbose_name='課題'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', to_field='username', verbose_name='ユーザ'),
        ),
    ]
