# Generated by Django 5.1.5 on 2025-02-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0034_admissionreview1_delete_admissionreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionreview1',
            name='apply',
            field=models.CharField(default='applied', max_length=20),
        ),
        migrations.AddField(
            model_name='admissionreview1',
            name='benefit',
            field=models.CharField(default='Benefits', max_length=20),
        ),
        migrations.AddField(
            model_name='admissionreview1',
            name='country_code',
            field=models.CharField(default='IN', max_length=5),
        ),
    ]
