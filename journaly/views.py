from .models import Journal
from django.views.generic import ListView


class JournalListView(ListView):
    model = Journal
    template_name = "journal_list.html"
    context_object_name = "journal_list"