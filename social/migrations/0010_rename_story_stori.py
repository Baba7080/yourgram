# Generated by Django 3.2.6 on 2021-09-07 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_rename_story_user_story_user'),
        ('social', '0009_story'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='story',
            new_name='stori',
        ),
    ]