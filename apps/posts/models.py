from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:20]
