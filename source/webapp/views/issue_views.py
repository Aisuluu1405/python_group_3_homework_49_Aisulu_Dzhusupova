from django.http import HttpResponseRedirect
from django.shortcuts import reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue, Project, Team, STATUS_OTHER_CHOICE
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from webapp.views.base_view import SessionUserMixin


class IndexView(SessionUserMixin, ListView):
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['id']
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.set_request(request)
        self.page_login()
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


class IssueView(SessionUserMixin, DetailView):
    model = Issue
    template_name = 'issue/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'issue'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


class IssueCreateView(LoginRequiredMixin, SessionUserMixin, CreateView):
    template_name = 'issue/add.html'
    model = Issue
    form_class = IssueForm

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class IssueProjectCreateView(UserPassesTestMixin, SessionUserMixin, CreateView):
    template_name = 'bonus/issue_add.html'
    model = Issue
    form_class = IssueForm

    def test_func(self):
        project = self.get_project()
        user_project = Project.objects.filter(project_team__user=self.request.user, project_team__finish=None)
        # print(issue_project)
        # print(user_project)
        return project in user_project

    def get_project(self):
        project_pk = self.kwargs['pk']
        return get_object_or_404(Project, pk=project_pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_pk = self.kwargs.get('pk')
        users_project = Project.objects.filter(pk=project_pk,
                                               status__icontains=STATUS_OTHER_CHOICE).values('pk')
        kwargs['current_project'] = users_project
        return kwargs

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        self.object = project.issues.create(**form.cleaned_data)
        self.object.created_by = self.request.user
        self.object.save()
        return redirect('webapp:project_new_index')

    def get_success_url(self):
        return reverse('webapp:project_new_index')

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)



class IssueEditView(UserPassesTestMixin, SessionUserMixin, UpdateView):
    template_name = 'issue/edit.html'
    model = Issue
    form_class = IssueForm
    context_object_name = 'issue'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['current_project'] = Project.objects.filter(issues=self.object)
        return kwargs


    def test_func(self):
        issue_project = self.get_object().project
        user_project = Project.objects.filter(project_team__user=self.request.user, project_team__finish=None)
        return issue_project in user_project

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_new_index')


class IssueDeleteView(UserPassesTestMixin, SessionUserMixin, DeleteView):
    model = Issue
    template_name = 'issue/delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('webapp:project_new_index')

    def test_func(self):
        issue_project = self.get_object().project
        user_project = Project.objects.filter(project_team__user=self.request.user, project_team__finish=None)
        print(user_project)
        return issue_project in user_project

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)
