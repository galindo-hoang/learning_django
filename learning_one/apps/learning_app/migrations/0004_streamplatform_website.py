# Generated by Django 4.1.1 on 2022-09-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0003_remove_streamplatform_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamplatform',
            name='website',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
