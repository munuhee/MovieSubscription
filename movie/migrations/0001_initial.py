# Generated by Django 5.0 on 2023-12-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('description', models.TextField()),
                ('directors', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duration in minutes')),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_images/')),
                ('video_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='youtube video id')),
                ('subscription_required', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='movie.tag')),
            ],
        ),
    ]
