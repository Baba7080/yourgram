# Generated by Django 3.2.6 on 2021-08-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='sno',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
    ]