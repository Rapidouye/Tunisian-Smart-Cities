# Generated by Django 3.2 on 2021-04-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_message_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
