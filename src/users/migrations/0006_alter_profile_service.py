# Generated by Django 4.0.3 on 2022-03-17 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.service'),
        ),
    ]
