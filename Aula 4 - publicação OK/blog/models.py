from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:50]  # Retorna os primeiros 50 caracteres do conteúdo

