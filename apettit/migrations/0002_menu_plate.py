# Generated by Django 2.2.6 on 2019-10-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apettit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='plate',
            field=models.ImageField(default='apettito/menu/static', upload_to='img'),
        ),
    ]
