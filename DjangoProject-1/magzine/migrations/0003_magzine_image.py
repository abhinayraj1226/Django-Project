# Generated by Django 3.2.1 on 2021-05-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magzine', '0002_remove_magzine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='magzine',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
