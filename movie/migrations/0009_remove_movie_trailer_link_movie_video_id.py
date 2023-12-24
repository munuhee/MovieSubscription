# Generated by Django 5.0 on 2023-12-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_tag_movie_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailer_link',
        ),
        migrations.AddField(
            model_name='movie',
            name='video_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='youtube video id'),
        ),
    ]
