# Generated by Django 2.0.6 on 2018-10-18 09:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='main_file',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
