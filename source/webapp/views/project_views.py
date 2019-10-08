from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('date_create')


class ProjectView(DetailView):
    model = Project
    template_name = 'project/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-create')
        context['issues'] = issues
        return context
