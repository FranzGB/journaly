from .models import Journal, JournalEntry
from django.views.generic import ListView, DetailView


class JournalView(ListView):
    """View Class for home page of site"""

    template_name = "journal_list.html"
    model = Journal
    context_object_name = "journal_list"

    # # Generate counts of some of the main objects
    # num_journals = Journal.objects.all().count()
    # num_entries = JournalEntry.objects.all().count()


class JournalEntryListView(ListView):
    template_name = "journal_entry_list.html"
    model = JournalEntry
    context_object_name = "journal_entry_list"


class JournalEntryView(DetailView):
    template_name = "journal_entry.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journal_entry"] = JournalEntry.objects.get(pk=kwargs["pk"])
        return context
