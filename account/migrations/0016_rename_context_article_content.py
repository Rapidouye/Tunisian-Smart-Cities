# Generated by Django 3.2 on 2021-04-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_rename_candidature_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='context',
            new_name='content',
        ),
    ]
