# Generated by Django 2.0.4 on 2018-06-12 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import geoposition.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('stage_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['stage_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Music Genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
                'verbose_name_plural': 'points of interest',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('album', models.TextField(help_text='Album Name', max_length=200)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Artist')),
                ('genre', models.ManyToManyField(help_text='Select Genre', to='catalog.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='SongInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique for each song', primary_key=True, serialize=False)),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Song')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField(help_text='This is a help text', verbose_name='My video')),
            ],
        ),
    ]
