# Generated by Django 3.1.3 on 2021-01-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210121_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.DateField(),
        ),
    ]
