# Generated by Django 4.0 on 2024-03-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_alter_ticket_ticket_holder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date_time',
        ),
        migrations.AddField(
            model_name='ticket',
            name='allow_resale',
            field=models.BooleanField(default=False),
        ),
    ]
