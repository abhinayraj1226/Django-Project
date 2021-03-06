# Generated by Django 3.2.1 on 2021-05-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magzine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Backround_Color', models.CharField(default=None, max_length=20)),
                ('title_font_size', models.IntegerField(default=None)),
                ('body_font_size', models.IntegerField(default=None)),
                ('title_text', models.CharField(default=None, max_length=20)),
                ('body_text', models.CharField(default=None, max_length=200)),
                ('title_color', models.CharField(default=None, max_length=20)),
                ('body_color', models.CharField(default=None, max_length=20)),
                ('image', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
    ]
