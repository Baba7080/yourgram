# Generated by Django 3.2.6 on 2021-08-29 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20210828_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='Post_pics'),
        ),
    ]
