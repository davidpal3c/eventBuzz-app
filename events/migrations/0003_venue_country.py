# Generated by Django 5.0.6 on 2024-05-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_venue_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='country',
            field=models.CharField(default='Unknown', max_length=40),
        ),
    ]
