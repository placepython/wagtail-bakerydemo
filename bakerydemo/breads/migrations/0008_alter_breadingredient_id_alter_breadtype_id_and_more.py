# Generated by Django 5.1.2 on 2024-10-12 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("breads", "0007_alter_breadingredient_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breadingredient",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="breadtype",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
