# Generated by Django 4.2 on 2023-05-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
