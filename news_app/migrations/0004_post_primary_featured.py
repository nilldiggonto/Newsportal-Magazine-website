# Generated by Django 3.2.5 on 2021-08-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_auto_20210801_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='primary_featured',
            field=models.BooleanField(default=True),
        ),
    ]