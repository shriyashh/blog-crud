# Generated by Django 3.2.4 on 2021-06-27 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0021_alter_blogpost_blogpostimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blogpostimage',
        ),
    ]
