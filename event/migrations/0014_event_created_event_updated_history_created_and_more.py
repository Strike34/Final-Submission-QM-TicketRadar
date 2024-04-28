# Generated by Django 4.0 on 2024-03-09 19:23

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='history',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 9, 19, 22, 53, 164329, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]