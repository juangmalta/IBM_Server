# Generated by Django 4.1.7 on 2023-05-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_control", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificaciones",
            name="issue_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
