# Generated by Django 4.1.7 on 2023-04-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
