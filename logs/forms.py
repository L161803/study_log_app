from django import forms
from .models import StudyLog

class StudyLogForm(forms.ModelForm):
    class Meta:
        model = StudyLog
        fields = ["subject", "study_time", "content"]
        labels = {
            "subject": "科目名",
            "study_time": "学習時間（分）",
            "content": "メモ"
        }