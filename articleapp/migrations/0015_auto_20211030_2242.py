# Generated by Django 3.2.7 on 2021-10-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0014_auto_20211030_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='weight',
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name='starpoint',
            name='star_point',
            field=models.IntegerField(default=3, null=True),
        ),
    ]
