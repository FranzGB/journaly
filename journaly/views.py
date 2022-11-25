from .models import Journal, JournalEntry
from django.views.generic import ListView
from django.shortcuts import render


def base(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_journals = Journal.objects.all().count()
    num_entries = JournalEntry.objects.all().count()
    context = {
        "num_journals": num_journals,
        "num_entries": num_entries,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, "base.html", context=context)


class JournalListView(ListView):
    model = Journal
    template_name = "journal_list.html"
    context_object_name = "journal_list"


class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "journal_entry_list.html"
    context_object_name = "journal_entry_list"
