# Generated by Django 4.2.6 on 2023-10-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustommodel',
            name='my_custom_file_field',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
