# Generated by Django 2.1.4 on 2018-12-20 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingmodel',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listingmodel',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='properties'),
        ),
        migrations.AlterField(
            model_name='listingmodel',
            name='photo_main',
            field=models.ImageField(blank=True, default='', upload_to='properties'),
        ),
    ]
