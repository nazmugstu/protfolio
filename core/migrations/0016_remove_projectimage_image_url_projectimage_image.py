# Generated by Django 5.2 on 2025-05-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
