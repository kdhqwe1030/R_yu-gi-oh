# Generated by Django 5.0.4 on 2024-05-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Ryugiohproject_app", "0002_rename_description_card_desc_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="set_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
