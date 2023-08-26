from django.db import models
from django.contrib.auth.models import User
from flashcards.models import Flashcard

# Create your models here.
class StudyPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target_certification = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    daily_study_time = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    
class StudyPlanFlashcard(models.Model):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    learned = models.BooleanField(default=False)
    last_reviewed = models.DateTimeField(null=True, blank=True)
