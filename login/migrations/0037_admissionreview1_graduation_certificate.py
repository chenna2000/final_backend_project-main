# Generated by Django 5.1.5 on 2025-02-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionreview1',
            name='graduation_certificate',
            field=models.FileField(blank=True, null=True, upload_to='uploads/graduation_certificates/'),
        ),
    ]
