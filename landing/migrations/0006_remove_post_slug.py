# Generated by Django 3.2.6 on 2021-08-29 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_remove_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]