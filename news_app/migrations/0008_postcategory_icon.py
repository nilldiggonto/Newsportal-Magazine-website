# Generated by Django 3.2.5 on 2021-08-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_postsubcategory_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='icon',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
