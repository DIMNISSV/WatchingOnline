# Generated by Django 4.1.3 on 2022-12-17 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orig_title',
            new_name='title_orig',
        ),
    ]