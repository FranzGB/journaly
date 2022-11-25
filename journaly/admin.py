from django.contrib import admin
from .models import JournalEntry, Journal


@admin.register(JournalEntry, Journal)
class JournalAdmin(admin.ModelAdmin):
    pass
