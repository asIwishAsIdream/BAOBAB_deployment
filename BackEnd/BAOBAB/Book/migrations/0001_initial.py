# Generated by Django 4.1 on 2023-07-29 12:02

import Book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Category", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookInfo",
            fields=[
                ("book_id", models.AutoField(primary_key=True, serialize=False)),
                ("book_Name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=20)),
                ("is_popular", models.BooleanField(default=False)),
                ("publication_year", models.CharField(max_length=20)),
                ("publication_month", models.CharField(max_length=10)),
                (
                    "mainCategory",
                    models.OneToOneField(
                        blank=True,
                        default="미분류",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="mainCategory",
                        to="Category.category",
                        validators=[Book.models.main_category_validator],
                    ),
                ),
                (
                    "subCategory",
                    models.OneToOneField(
                        blank=True,
                        default="미분류",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="subCategory",
                        to="Category.category",
                        validators=[Book.models.sub_category_validator],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookStats",
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
                ("rating", models.FloatField(default=0.0)),
                ("liked", models.IntegerField(default=0)),
                ("views", models.IntegerField(default=0)),
                (
                    "book_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Book.bookinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookFile",
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
                ("book_file", models.FileField(upload_to="")),
                (
                    "book_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Book.bookinfo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookCover",
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
                ("book_cover", models.ImageField(upload_to="")),
                (
                    "book_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Book.bookinfo"
                    ),
                ),
            ],
        ),
    ]