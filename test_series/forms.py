from django import forms
from .models import ExamParticipant, ProctoringEvent

class StartProctoringSessionForm(forms.Form):
    exam_id = forms.IntegerField()
    duration = forms.DurationField(required=False, help_text="Duration of the session (e.g., '1:30:00' for 1 hour 30 minutes)")

class EndProctoringSessionForm(forms.Form):
    session_id = forms.IntegerField()

class RecordProctoringEventForm(forms.ModelForm):
    session_id = forms.IntegerField()

    class Meta:
        model = ProctoringEvent
        fields = ['event_type', 'details', 'session_id']

class SubmitAnswerForm(forms.Form):
    session_id = forms.IntegerField()
    question_no = forms.IntegerField()
    selected_option = forms.CharField(max_length=255)
    clear_response = forms.BooleanField(required=False)

class MarkForReviewForm(forms.Form):
    session_id = forms.IntegerField()
    question_no = forms.IntegerField()
    mark = forms.BooleanField(required=True)

class SubmitAllAnswersForm(forms.Form):
    session_id = forms.IntegerField()
    answers = forms.JSONField()

class ExamParticipantForm(forms.ModelForm):
    class Meta:
        model = ExamParticipant
        fields = ['name', 'email', 'phone_number']

from django import forms
from .models import AdmissionReview

class Step1Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview
        fields = [
            "college_name", "other_college_name", "course_name", "other_course_name",
            "student_name", "email", "phone_number", "gender",
            "linkedin_profile", "course_fees", "year", "referral_code",
            "anvil_reservation_benefits", "gd_pi_admission", "class_size",
            "opted_hostel", "college_provides_placements", "hostel_fees", "average_package"
        ]

class Step2Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview
        fields = ["admission_process", "course_curriculum_faculty"]

class Step3Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview
        fields = ["fees_structure_scholarship"]

class Step4Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview
        fields = ["liked_things", "disliked_things"]

class Step5Form(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    campus_photos = forms.ImageField(required=False)

    class Meta:
        model = AdmissionReview
        fields = ["profile_photo", "campus_photos", "agree_terms"]

class Step6Form(forms.ModelForm):
    certificate_id_card = forms.FileField(required=False)

    class Meta:
        model = AdmissionReview
        fields = ["certificate_id_card"]
