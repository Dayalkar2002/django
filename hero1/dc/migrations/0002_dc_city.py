# Generated by Django 5.0.1 on 2024-01-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc',
            name='city',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
