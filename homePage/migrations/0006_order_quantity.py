# Generated by Django 4.2.3 on 2023-07-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0005_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
