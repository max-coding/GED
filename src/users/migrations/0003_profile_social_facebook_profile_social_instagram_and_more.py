# Generated by Django 4.0.3 on 2022-03-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
