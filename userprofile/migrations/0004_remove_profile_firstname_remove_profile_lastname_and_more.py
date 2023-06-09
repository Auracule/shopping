# Generated by Django 4.1.7 on 2023-04-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_profile_pix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(default='a', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(default='profile.jpg', upload_to='Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='a', max_length=100),
        ),
    ]
