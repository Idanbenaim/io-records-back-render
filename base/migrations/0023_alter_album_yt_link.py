# Generated by Django 4.2.2 on 2023-09-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_album_yt_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='yt_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
