from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import FormView
from webapp.forms import UserProjectForm
from webapp.models import Team, Project
from webapp.views.base_view import SessionUserMixin


class TeamUpdateView(PermissionRequiredMixin, SessionUserMixin, FormView):
    template_name = 'team/add_user.html'
    form_class = UserProjectForm
    permission_required = 'webapp.change_team'
    permission_denied_message = 'Access is denied!'

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        users_list = list(form.cleaned_data.pop('project_user'))
        project_users = Team.objects.filter(project=project, finish=None)

        for user in users_list:
            if user not in project_users:
                Team.objects.create(user=user, project=project, start=datetime.now())
        for user in project_users:
            if user not in users_list:
                user.finish = datetime.now()
                user.save()
        return redirect('webapp:project_new_detail', pk=project_pk)


    def get(self, request, *args, **kwargs):
        self.set_request(request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        initial = super().get_initial()
        initial['project_user'] = User.objects.filter(user_team__project=project, user_team__finish=None)
        return initial


    def get_success_url(self):
        return reverse('webapp:project_new_index')
