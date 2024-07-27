# Generated by Django 5.0.6 on 2024-07-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_merchantsponsers_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grandeventsystem',
            name='EventStatus',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], help_text='Select the current status of the event.', max_length=20),
        ),
    ]