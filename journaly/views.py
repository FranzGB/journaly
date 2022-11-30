from .models import Journal, JournalEntry
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


class JournalView(ListView):
    """View Class for home page of site"""

    template_name = "journals/journal_list.html"
    model = Journal
    context_object_name = "journal_list"

    # # Generate counts of some of the main objects
    # num_journals = Journal.objects.all().count()
    # num_entries = JournalEntry.objects.all().count()


class JournalEntryListView(ListView):
    template_name = "entries/journal_entry_list.html"
    model = JournalEntry
    context_object_name = "journal_entry_list"

    def get_form_url(self):
        return reverse("journal-entry-form", kwargs={"slug": self.object.journal.slug})


class JournalEntryView(DetailView):
    template_name = "entries/journal_entry.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journal_entry"] = JournalEntry.objects.get(pk=kwargs["pk"])
        return context


class JournalCreateView(CreateView):
    template_name = "journals/journal_form.html"
    model = Journal
    fields = "__all__"
    success_url = reverse_lazy("journals")


class EntryCreateView(CreateView):
    template_name = "entries/journal_entry_form.html"
    model = JournalEntry
    fields = "_all_"
