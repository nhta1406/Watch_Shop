# Generated by Django 5.0.4 on 2024-05-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_account_idac"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="NgayTao",
            field=models.DateField(auto_now_add=True),
        ),
    ]
