# Generated by Django 4.1.5 on 2023-01-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_remove_message_name_gallary_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]