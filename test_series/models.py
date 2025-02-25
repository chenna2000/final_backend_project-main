from django.db import models
from django.utils import timezone
from login.models import new_user

class Exam(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

class ProctoringSession(models.Model):
    user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(default=timezone.timedelta(hours=3))
    is_submitted = models.BooleanField(default=False)

    STATUS_CHOICES = [
        ('ongoing', 'ongoing'),
        ('completed', 'completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ongoing')

class ProctoringEvent(models.Model):
    # user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    session = models.ForeignKey(ProctoringSession, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

class Question(models.Model):
    user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_no = models.IntegerField(unique=True)
    question_text = models.TextField(default="Default question text")
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255,default='option1')
    section = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    duration = models.DurationField(default=timezone.timedelta(hours=3))

class UserResponse(models.Model):
    user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # response = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    # end_time = models.DateTimeField(null=True, blank=True)
    session = models.ForeignKey(ProctoringSession, on_delete=models.CASCADE)
    marked_for_review = models.BooleanField(default=False)
    selected_option = models.CharField(max_length=255,default='option1')
    response_time = models.DateTimeField(default=timezone.now)


class UserScore(models.Model):
    user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class ExamParticipant(models.Model):
    # user = models.ForeignKey(new_user, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    exam_started = models.BooleanField(default=False)

class AdmissionReview(models.Model):
    college_name = models.CharField(max_length=255)
    other_college_name = models.CharField(max_length=255, blank=True, null=True)
    course_name = models.CharField(max_length=255)
    other_course_name = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    linkedin_profile = models.URLField(blank=True, null=True)
    course_fees = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    referral_code = models.CharField(max_length=50, blank=True, null=True)
    anvil_reservation_benefits = models.BooleanField(default=False)
    gd_pi_admission = models.BooleanField(default=False)
    class_size = models.PositiveIntegerField()
    opted_hostel = models.BooleanField(default=False)
    college_provides_placements = models.BooleanField(default=False)
    hostel_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    average_package = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    admission_process = models.TextField()
    course_curriculum_faculty = models.TextField()
    fees_structure_scholarship = models.TextField()
    liked_things = models.TextField()
    disliked_things = models.TextField()
    
    profile_photo = models.ImageField(upload_to="uploads/", blank=True, null=True)
    campus_photos = models.ImageField(upload_to="uploads/", blank=True, null=True)
    certificate_id_card = models.FileField(upload_to="uploads/", blank=True, null=True)
    
    agree_terms = models.BooleanField(default=False)
