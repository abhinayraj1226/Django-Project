# Generated by Django 3.2.1 on 2021-05-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcaptcha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcaptcha',
            name='num',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
