# Generated by Django 3.2.8 on 2022-03-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]