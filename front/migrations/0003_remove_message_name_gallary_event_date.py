# Generated by Django 4.1.5 on 2023-01-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_gallary_image_message_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.AddField(
            model_name='gallary',
            name='event_date',
            field=models.DateField(auto_now=True),
        ),
    ]
