# Generated by Django 3.1.8 on 2023-02-08 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20230208_1025'),
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='locations', to='users.BondableUser'),
        ),
        migrations.AddField(
            model_name='dayshift',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='homes.home'),
        ),
    ]