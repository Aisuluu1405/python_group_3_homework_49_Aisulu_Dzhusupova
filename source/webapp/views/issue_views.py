from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import IssueForm
from webapp.models import Issue, Project


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
    pk_url_kwarg = 'pk'
    context_object_name = 'issue'


class IssueCreateView(CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class IssueProjectCreateView(CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        project.issues.create(**form.cleaned_data)
        return redirect('project_detail',pk=project_pk)


class IssueEditView(UpdateView):
    template_name = 'issue/edit.html'
    model = Issue
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue/delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('index')


