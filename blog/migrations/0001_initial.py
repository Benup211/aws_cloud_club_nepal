# Generated by Django 5.0.6 on 2024-07-23 02:20

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWSBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('date_of_publish', models.DateField(auto_now=True)),
                ('profile', models.ImageField(upload_to='blog_profile')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField(max_length=200)),
                ('detail', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('read_time', models.IntegerField(default=2)),
            ],
        ),
    ]