# Generated by Django 4.1.3 on 2023-01-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('post', '0010_post_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated_at',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
    ]
