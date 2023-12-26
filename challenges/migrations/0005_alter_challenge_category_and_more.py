# Generated by Django 4.0 on 2023-12-26 06:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_alter_exercise_category_alter_exercise_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='category',
            field=models.CharField(choices=[('WebExploitation', 'WebExploitation'), ('Cryptography', 'Cryptography'), ('Reversing', 'Reversing'), ('Pwnable', 'Pwnable'), ('Forensics', 'Forensics'), ('Network', 'Network'), ('GenerallSkill', 'GenerallSkill'), ('Misc', 'Misc')], default='Misc', max_length=30, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='cleared_counts',
            field=models.IntegerField(default=0, verbose_name='正解者数'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='exerciseName',
            field=models.ForeignKey(default='実戦問題', on_delete=django.db.models.deletion.SET_DEFAULT, to='challenges.exercise', verbose_name='演習名'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='flag',
            field=models.CharField(default='', max_length=100, verbose_name='フラグ'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='hint_one',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ヒント1'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='hint_three',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ヒント3'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='hint_two',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ヒント2'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='identifier',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9a-zA-Z]*$')], verbose_name='識別子'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='problem',
            field=models.TextField(default='', verbose_name='問題文'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3000)], verbose_name='配点'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(default='', max_length=30, validators=[django.core.validators.RegexValidator(regex='^[0-9]{2}[.]{1}')], verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='visible',
            field=models.BooleanField(default=False, verbose_name='ユーザへの公開'),
        ),
    ]