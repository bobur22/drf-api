# Generated by Django 5.0.1 on 2024-01-27 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorsmodel',
            options={},
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jwt_token.authorsmodel'),
        ),
    ]
