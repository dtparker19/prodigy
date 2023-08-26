from django.db import models
from django.contrib.auth.models import User

class FlashcardTopic(models.Model):
    name = models.CharField(max_length=100)

class FlashcardDifficulty(models.Model):
    name = models.CharField(max_length=50)

class Flashcard(models.Model):
    topic = models.ForeignKey(FlashcardTopic, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(FlashcardDifficulty, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    ai_generated_explanation = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class FlashcardReview(models.Model):
    user = models.ForeignKey(User, on_delete=modelpys.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    reviewed_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField()
    notes = models.TextField(blank=True, null=True)