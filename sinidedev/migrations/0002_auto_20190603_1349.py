# Generated by Django 2.2.1 on 2019-06-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinidedev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.IntegerField(),
        ),
    ]
