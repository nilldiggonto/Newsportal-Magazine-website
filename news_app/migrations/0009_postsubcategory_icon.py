# Generated by Django 3.2.5 on 2021-08-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0008_postcategory_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsubcategory',
            name='icon',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
