# Generated by Django 3.1.3 on 2021-01-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210121_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
