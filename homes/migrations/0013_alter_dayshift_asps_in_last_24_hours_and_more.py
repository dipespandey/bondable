# Generated by Django 4.1.6 on 2023-02-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homes", "0012_dayshift_agency_hours_in_last_24_hours_carer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dayshift",
            name="ASPS_in_last_24_hours",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="dayshift",
            name="incidents_in_last_24_hours",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="monthlyshiftaggregate",
            name="occupancy",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weeklyshiftaggregate",
            name="occupancy",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
