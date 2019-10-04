from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView
from django.views import View
from webapp.forms import StatusForm
from webapp.models import Status
from django.db.models import ProtectedError


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


class StatusEditView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'status/edit.html', context={'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_index')
        else:
            return render(request, 'status/edit.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        return render(request, 'status/delete.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        try:
            status.delete()
            return redirect('status_index')
        except ProtectedError:
            return render(request, 'protected_error.html')

