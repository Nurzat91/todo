# Generated by Django 3.1.3 on 2021-01-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210121_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.DateField(auto_created=True),
        ),
    ]
