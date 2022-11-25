from django.db import models
from django.urls import reverse


class Journal(models.Model):
    journal_title = models.CharField(max_length=100, blank=False)
    content_description = models.TextField(
        max_length=400, blank=False, default="A generic journal"
    )
    slug = models.SlugField(max_length=50, unique=True, null=True)

    class Meta:
        ordering = ["journal_title"]

    def __str__(self):
        return self.journal_title

    def get_absolute_url(self):
        return reverse("journal-entry-list", kwargs={"slug": self.slug})

class JournalEntry(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_created"]
