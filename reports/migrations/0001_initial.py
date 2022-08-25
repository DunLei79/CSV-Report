# Generated by Django 4.1 on 2022-08-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reports",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ticket", models.CharField(max_length=255)),
                ("subject", models.CharField(blank=True, max_length=255, null=True)),
                ("status", models.CharField(blank=True, max_length=255, null=True)),
                ("agent", models.CharField(blank=True, max_length=255, null=True)),
                ("group", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "created_time",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "closed_time",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "time_tracked",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "first_response_time",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "resolution_status",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("tags", models.CharField(blank=True, max_length=255, null=True)),
                ("branch", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "branch_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("field_tech", models.CharField(blank=True, max_length=255, null=True)),
                ("call_type", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "printer_serial",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("km", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "travel_time",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("job_card", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "dell_call_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "customer_call_ref",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("area", models.CharField(blank=True, max_length=255, null=True)),
                ("parts_used", models.TextField(blank=True, max_length=255, null=True)),
                (
                    "closing_details",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("users", models.CharField(blank=True, max_length=255, null=True)),
                ("contactid", models.CharField(blank=True, max_length=255, null=True)),
                ("company", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]