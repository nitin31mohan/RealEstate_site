# Generated by Django 2.1.4 on 2018-12-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_remove_usermodel_is_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_profile_image',
            field=models.ImageField(blank=True, default='defaultDP.png', null=True, upload_to='user/'),
        ),
    ]