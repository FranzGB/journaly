from django.db import models


class Journal(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title
