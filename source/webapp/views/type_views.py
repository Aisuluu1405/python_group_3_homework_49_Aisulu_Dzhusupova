from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView
from django.views import View

from webapp.forms import TypeForm
from webapp.models import Type
from django.db.models import ProtectedError

from webapp.views.base_view import EditView, DeleteView


class TypeIndexView(ListView):
    template_name = 'type/index.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/add.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_index')


class TypeEditView(EditView):
    template_name = 'type/edit.html'
    model = Type
    form_class = TypeForm
    context_key = 'type'

    def get_redirect_url(self):
        return reverse('type_index')


class TypeDeleteView(DeleteView):
    model = Type
    template = 'protected_error.html'
    confirm_deletion = False

    def get_redirect_url(self):
        return reverse('type_index')

