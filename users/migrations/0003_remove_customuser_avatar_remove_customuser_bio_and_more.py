# Generated by Django 4.2.6 on 2024-11-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_customuser_date_of_birth_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="avatar",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="bio",
        ),
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]