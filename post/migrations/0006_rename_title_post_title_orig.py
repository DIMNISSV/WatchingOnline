# Generated by Django 4.1.3 on 2022-12-29 09:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0005_remove_dubworker_nickname_dubworker_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='title_orig',
        ),
    ]
