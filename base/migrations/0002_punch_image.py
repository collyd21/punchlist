# Generated by Django 4.1.5 on 2023-11-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='punch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='punch_images/'),
        ),
    ]