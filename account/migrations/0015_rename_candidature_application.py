# Generated by Django 3.2 on 2021-04-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_admin_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Candidature',
            new_name='Application',
        ),
    ]
