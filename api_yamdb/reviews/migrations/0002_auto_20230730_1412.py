# Generated by Django 3.2 on 2023-07-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-id'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
    ]
