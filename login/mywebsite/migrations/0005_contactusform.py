# Generated by Django 3.2 on 2021-04-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mywebsite', '0004_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactusForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.TextField(max_length=100)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]