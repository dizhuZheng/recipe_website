# Generated by Django 2.2.2 on 2019-09-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20190926_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('g', 'grams'), ('ml', 'ml')], default='g', max_length=2),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(default='', related_name='recipe_ingredient', to='recipes.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='sauce',
            field=models.ManyToManyField(default='', related_name='recipe_sauce', to='recipes.Sauce'),
        ),
    ]
