# Generated by Django 4.1.5 on 2023-03-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0003_remove_trash_player"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trash",
            name="image",
            field=models.ImageField(upload_to="images/trash_icons"),
        ),
    ]