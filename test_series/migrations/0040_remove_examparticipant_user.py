# Generated by Django 5.1.5 on 2025-02-14 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0039_proctoringsession_is_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examparticipant',
            name='user',
        ),
    ]
