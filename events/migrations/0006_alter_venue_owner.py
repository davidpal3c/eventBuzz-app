# Generated by Django 5.0.6 on 2024-05-21 23:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_approved'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Venue Owner'),
        ),
    ]



    def map_owner_id_to_user(apps, schema_editor):
        # This function will be called by Django's migration framework
        # It receives the 'apps' and 'schema_editor' parameters
        User = apps.get_model('auth.User')  # Assuming 'auth.User' is the correct model name
        Venue = apps.get_model('events.Venue')  # Replace 'events' with your app name

        # Map old owner IDs to new owner objects
        for venue in Venue.objects.all():
            owner_id = venue.owner
            owner = User.objects.get(id=owner_id)
            venue.owner = owner
            venue.save()

        print("Venue owner ID:", venue.owner_id)
        return [(owner.username, {owner_id: owner}), {}]

