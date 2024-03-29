# Generated by Django 2.2.2 on 2019-09-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pic_path', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
