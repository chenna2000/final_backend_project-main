# Generated by Django 5.1.5 on 2025-02-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0031_admissionreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionreview',
            name='agree_terms',
            field=models.BooleanField(default=False),
        ),
    ]
