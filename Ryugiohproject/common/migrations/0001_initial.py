# Generated by Django 4.1 on 2024-05-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserModel",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
