# Generated by Django 3.0.6 on 2020-06-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20200612_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
