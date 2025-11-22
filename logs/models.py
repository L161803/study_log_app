# logs/models.py
from django.db import models

# Create your models here.
class StudyLog(models.Model):
    #Subjects (ex. Math, English)
    subject = models.CharField(max_length=100)

    #Study Term (as minutes)
    study_time = models.IntegerField()

    #memo notes
    content = models.TextField()

    #Date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.study_time}分"

