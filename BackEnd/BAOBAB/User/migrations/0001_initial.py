# Generated by Django 4.1 on 2023-08-08 09:32

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("nickname", models.CharField(max_length=50, unique=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]