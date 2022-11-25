from .models import Journal, JournalEntry
from django.views.generic import ListView


class JournalListView(ListView):
    model = Journal
    template_name = "journal_list.html"
    context_object_name = "journal_list"


class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "journal_entry_list.html"
    context_object_name = "journal_entry_list"
