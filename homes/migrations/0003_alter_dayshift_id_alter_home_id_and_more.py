# Generated by Django 4.1.6 on 2023-02-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homes", "0002_auto_20230208_1025"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dayshift",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="home",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="monthlyshiftaggregate",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="weeklyshiftaggregate",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
