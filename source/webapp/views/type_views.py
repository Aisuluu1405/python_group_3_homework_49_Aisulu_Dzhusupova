from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import TypeForm
from webapp.models import Type
from django.db.models import ProtectedError


class TypeIndexView(ListView):
    template_name = 'type/index.html'
    context_object_name = 'types'
    model = Type


class TypeCreateView(CreateView):
    template_name = 'type/add.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:type_index')


class TypeEditView(UpdateView):
    template_name = 'type/edit.html'
    model = Type
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('webapp:type_index')


class TypeDeleteView(DeleteView):
    model = Type
    success_url = reverse_lazy('webapp:type_index')
    template = 'type/protected_error.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            return render(request, self.template)
