# Generated by Django 4.0 on 2024-03-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_ticket_reference_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='available_tickets',
            field=models.IntegerField(default=50),
        ),
    ]
