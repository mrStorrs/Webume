# Generated by Django 3.0.6 on 2020-05-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_projects_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='color',
            field=models.CharField(default='white', max_length=5),
        ),
    ]