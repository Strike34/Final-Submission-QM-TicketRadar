# Generated by Django 4.0 on 2024-03-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_remove_event_resell_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]