# Generated by Django 3.1.7 on 2021-03-17 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20210316_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='topics',
            new_name='topic',
        ),
    ]