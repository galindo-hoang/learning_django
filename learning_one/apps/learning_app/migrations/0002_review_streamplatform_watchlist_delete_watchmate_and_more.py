# Generated by Django 4.1.1 on 2022-09-13 16:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)])),
                ('description', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=150)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('storyline', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='learning_app.streamplatform')),
            ],
        ),
        migrations.DeleteModel(
            name='WatchMate',
        ),
        migrations.AddField(
            model_name='review',
            name='watchlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='learning_app.watchlist'),
        ),
    ]
