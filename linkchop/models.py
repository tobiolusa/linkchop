from django.db import models

# URL model

class Link(models.Model):
    original_url = models.URLField()
    shorten_code = models.CharField(max_length=10, unique=True)
    created_now = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url

