from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('date_create')
