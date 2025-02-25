# Generated by Django 5.1.5 on 2025-02-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0042_remove_userresponse_end_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=255)),
                ('other_college_name', models.CharField(blank=True, max_length=255, null=True)),
                ('course_name', models.CharField(max_length=255)),
                ('other_course_name', models.CharField(blank=True, max_length=255, null=True)),
                ('student_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('course_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField()),
                ('referral_code', models.CharField(blank=True, max_length=50, null=True)),
                ('anvil_reservation_benefits', models.BooleanField(default=False)),
                ('gd_pi_admission', models.BooleanField(default=False)),
                ('class_size', models.PositiveIntegerField()),
                ('opted_hostel', models.BooleanField(default=False)),
                ('college_provides_placements', models.BooleanField(default=False)),
                ('hostel_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('average_package', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('admission_process', models.TextField()),
                ('course_curriculum_faculty', models.TextField()),
                ('fees_structure_scholarship', models.TextField()),
                ('liked_things', models.TextField()),
                ('disliked_things', models.TextField()),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('campus_photos', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('certificate_id_card', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('agree_terms', models.BooleanField(default=False)),
            ],
        ),
    ]
