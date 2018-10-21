# Generated by Django 2.1.2 on 2018-10-19 17:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0023_auto_20181019_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, help_text='This slug will form the url of your blog. The Url will be blogs/blog/<your username>/<slug>', max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together={('slug', 'author', 'title')},
        ),
    ]
