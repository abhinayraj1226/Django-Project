# Generated by Django 3.2.1 on 2021-05-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arithmetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.IntegerField(default=None)),
                ('input2', models.IntegerField(default=None)),
                ('operations', models.CharField(default=None, max_length=20)),
            ],
        ),
    ]