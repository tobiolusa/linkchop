# Generated by Django 5.2.1 on 2025-05-07 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkchop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='shorten_url',
            new_name='shorten_code',
        ),
    ]
