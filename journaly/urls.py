"""journaly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("journals/", views.JournalView.as_view(), name="journals"),
    path(
        "journals/create",
        views.JournalCreateView.as_view(),
        name="journal-form"),
    path(
        "journals/<slug:slug>",
        views.JournalEntryListView.as_view(),
        name="journal-entry-list",
    ),
    path(
        "journals/<slug:slug>/new",
        views.EntryCreateView.as_view(),
        name="journal-entry-form"
    ),
    path("__reload__/", include("django_browser_reload.urls")),
]
