# Generated by Django 5.1.6 on 2025-03-07 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postreaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postreaction',
            old_name='gender',
            new_name='reaction_type',
        ),
    ]
