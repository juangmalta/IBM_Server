# Generated by Django 4.1.7 on 2023-06-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_useractivities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=8),
        ),
    ]