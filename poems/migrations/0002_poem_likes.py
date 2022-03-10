# Generated by Django 3.2 on 2022-03-10 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='poem_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
