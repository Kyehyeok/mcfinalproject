# Generated by Django 3.2.7 on 2021-10-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0005_alter_ingredientunique_bigcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientunique',
            name='bigcat',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
