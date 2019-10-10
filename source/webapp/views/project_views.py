from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project, STATUS_OTHER_CHOICE, PROJECT_CLOSED


class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('date_create')


class ProjectIndexNewView(ListView):
    template_name = 'project/index_project_new.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('date_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_closed'] = Project.objects.all().filter(status=PROJECT_CLOSED)
        context['project_active'] = Project.objects.all().filter(status=STATUS_OTHER_CHOICE)
        return context


class ProjectView(DetailView):
    model = Project
    template_name = 'project/detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = context['project'].issues.order_by('-create')
        context['issues'] = issues
        return context


class ProjectNewView(DetailView):
    model = Project
    template_name = 'project/detail_new.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = context['project'].issues.order_by('-create')
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


class ProjectNewDeleteView(UpdateView):
    model = Project
    success_url = reverse_lazy('project_new_index')

    def get(self, request, *args, **kwargs):
        object = self.model.objects.filter(pk=kwargs.get('pk'))
        object.update(status='closed')
        return redirect(self.success_url)

