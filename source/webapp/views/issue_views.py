from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue, Project, Team
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['id']
    paginate_by = 5
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(). get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset=queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class IssueView(DetailView):
    model = Issue
    template_name = 'issue/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'issue'


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class IssueProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm


    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        project.issues.create(**form.cleaned_data)
        return redirect('webapp:project_detail', pk=project_pk)


class IssueEditView(UserPassesTestMixin, UpdateView):
    template_name = 'issue/edit.html'
    model = Issue
    form_class = IssueForm
    context_object_name = 'issue'

    def test_func(self):
        issue_project = self.get_object().project
        user_project = Project.objects.filter(project_team__user=self.request.user, project_team__finish=None)
        print(user_project)
        return issue_project in user_project

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = 'issue/delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        issue_project = self.get_object().project
        user_project = Project.objects.filter(project_team__user=self.request.user, project_team__finish=None)
        print(user_project)
        return issue_project in user_project
