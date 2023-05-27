# Generated by Django 4.1.7 on 2023-05-27 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("computerApp", "0029_machine_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="machine",
            name="user",
        ),
        migrations.AddField(
            model_name="machine",
            name="utilisateur",
            field=models.ForeignKey(
                default="default",
                on_delete=django.db.models.deletion.CASCADE,
                to="computerApp.utilisateur",
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="machine",
            name="mach",
            field=models.CharField(
                choices=[
                    ("PC", "PC - Run Windows"),
                    ("Mac", "Mac - Run MacOS"),
                    ("Serveur", "Serveur - Simple Server to deploy virtual machines"),
                    ("Switch", "Switch - To maintain and connect servers"),
                ],
                default="PC",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="utilisateur",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
