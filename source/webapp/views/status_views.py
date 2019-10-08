from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import StatusForm
from webapp.models import Status


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


class StatusEditView(UpdateView):
    template_name = 'status/edit.html'
    model = Status
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_index')


class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('status_index')
    template = 'status/protected_error.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            return render(request, self.template)
