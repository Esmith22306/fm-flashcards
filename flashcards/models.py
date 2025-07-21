from django.db import models

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
