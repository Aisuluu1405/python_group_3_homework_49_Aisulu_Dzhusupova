from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project, STATUS_OTHER_CHOICE, PROJECT_CLOSED, Team
from webapp.views.base_view import SessionUserMixin


class ProjectIndexNewView(SessionUserMixin, ListView):
    template_name = 'bonus/index_project_new.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('date_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_closed'] = Project.objects.all().filter(status=PROJECT_CLOSED)
        context['project_active'] = Project.objects.all().filter(status=STATUS_OTHER_CHOICE)
        return context

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


class ProjectNewView(SessionUserMixin, DetailView):
    model = Project
    template_name = 'bonus/detail_new.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = context['project'].issues.order_by('-create')
        context['issues'] = issues
        return context

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)


class ProjectCreateView(LoginRequiredMixin, SessionUserMixin, CreateView):
    template_name = 'project/add.html'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        users = form.cleaned_data.pop('user_project')
        user_project = self.request.user
        users_list = list(users)
        users_list.append(user_project)
        self.object = form.save()
        for user in users_list:
            Team.objects.create(user=user, project=self.object, start=datetime.now())
        return redirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_new_index')


class ProjectEditView(LoginRequiredMixin, SessionUserMixin, UpdateView):
    template_name = 'project/edit.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class ProjectNewDeleteView(LoginRequiredMixin, SessionUserMixin, UpdateView):
    model = Project
    success_url = reverse_lazy('webapp:project_new_index')

    def get(self, request, *args, **kwargs):
        object = self.model.objects.filter(pk=kwargs.get('pk'))
        object.update(status='closed')
        self.set_request(request)
        self.page_login()

        return redirect(self.success_url)
