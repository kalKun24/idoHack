# Generated by Django 4.0 on 2023-11-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomation',
            name='category',
            field=models.CharField(choices=[('update', 'アップデート'), ('infomation', 'お知らせ'), ('competition', '競技情報'), ('maintenance', 'メンテナンス')], default='infomation', max_length=30),
        ),
    ]
