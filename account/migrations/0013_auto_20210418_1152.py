# Generated by Django 3.2 on 2021-04-18 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210418_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='context',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.admin'),
        ),
    ]