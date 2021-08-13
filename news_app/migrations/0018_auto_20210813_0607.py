# Generated by Django 3.2.5 on 2021-08-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0017_alter_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postsubcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postsubcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
