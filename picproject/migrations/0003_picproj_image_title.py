# Generated by Django 5.0.2 on 2024-05-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picproject', '0002_picproj_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='picproj',
            name='image_title',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
