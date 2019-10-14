# Generated by Django 2.2.2 on 2019-10-11 00:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20191011_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(default=1, verbose_name=django.core.validators.MaxValueValidator(limit_value=5)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=3, verbose_name=django.core.validators.MaxValueValidator(limit_value=5)),
        ),
        migrations.AlterField(
            model_name='sauce',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]
