from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView
from django.views import View
from webapp.views.base_view import DetailView, EditView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['id']
    paginate_by = 5
    paginate_orphans = 1


class IssueView(DetailView):
    model = Issue
    template_name = 'issue/detail.html'
    context_key = 'issue'


class IssueCreateView(CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class IssueEditView(EditView):
    template_name = 'issue/edit.html'
    model = Issue
    form_class = IssueForm
    context_key = 'issue'


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue/delete.html'
    context_key = 'issue'


    def get_redirect_url(self):
        return reverse('index')
