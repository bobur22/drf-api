# Generated by Django 5.0.1 on 2024-01-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_modulemodel_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulemodel',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='module_students', to='school.studentmodel'),
        ),
    ]
