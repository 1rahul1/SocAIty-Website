# Generated by Django 2.1.2 on 2018-10-20 17:23

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20181020_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Please select one or more tags for your blog or create a new tag', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=15, unique=True, validators=[blog.models.tag_name_validator], verbose_name='Tag Name'),
        ),
    ]