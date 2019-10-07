from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView
from django.views import View
from webapp.forms import StatusForm
from webapp.models import Status
from django.db.models import ProtectedError
from webapp.views.base_view import EditView, DeleteView


class StatusIndexView(ListView):
    template_name = 'status/index.html'
    context_object_name = 'statuses'
    model = Status


class StatusCreateView(CreateView):
    template_name = 'status/add.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_index')


class StatusEditView(EditView):
    template_name = 'status/edit.html'
    model = Status
    form_class = StatusForm
    context_key = 'status'

    def get_redirect_url(self):
        return reverse('status_index')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete.html'
    context_key = 'status'
    template = 'protected_error.html'


    def get_redirect_url(self):
        return reverse('status_index')
