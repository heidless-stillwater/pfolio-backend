# Generated by Django 3.2.12 on 2024-06-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
