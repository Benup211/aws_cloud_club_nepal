# Generated by Django 5.0.6 on 2024-07-09 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestspeaker',
            options={'verbose_name': 'AWS Guest Speaker', 'verbose_name_plural': 'AWS Guest Speakers'},
        ),
    ]
