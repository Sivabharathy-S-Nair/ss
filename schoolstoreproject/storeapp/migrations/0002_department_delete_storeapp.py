# Generated by Django 4.2.6 on 2024-01-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='photo')),
            ],
        ),
        migrations.DeleteModel(
            name='storeapp',
        ),
    ]
