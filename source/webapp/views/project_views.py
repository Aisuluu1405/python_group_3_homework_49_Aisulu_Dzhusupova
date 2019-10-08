from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
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


class ProjectCreateView(CreateView):
    template_name = 'project/add.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectEditView(UpdateView):
    template_name = 'project/edit.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_index')
    template = 'project/protected_error.html'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            return render(request, self.template)
