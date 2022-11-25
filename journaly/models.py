from django.db import models


class Journal(models.Model):
    journal_title = models.CharField(max_length=100, blank=False)
    content_description = models.TextField(
        max_length=400, blank=False, default="A generic journal"
    )

    class Meta:
        ordering = ["journal_title"]

    def __str__(self):
        return self.title


class JournalEntry(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_created"]
