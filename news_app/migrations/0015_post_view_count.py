# Generated by Django 3.2.5 on 2021-08-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0014_rename_auhor_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]