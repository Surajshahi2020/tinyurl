from django.db import models
from django.utils.timezone import now


class ShortenedURLStore(models.Model):
    original_url = models.URLField(max_length=2000, unique=True)
    custom_url = models.CharField(max_length=50, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"ShortenedURL: {self.original_url}--{self.created_at}"
