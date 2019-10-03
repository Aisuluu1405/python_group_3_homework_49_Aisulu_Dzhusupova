from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from webapp.views.base_view import DetailView

from webapp.forms import IssueForm
from webapp.models import Issue


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
    context_key = 'issue'


class IssueCreateView(View):

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('detail', pk=issue.pk)
        else:
            return render(request, 'issue/add.html', context={'form': form})


class IssueEditView(View):

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id
        })
        return render(request, 'issue/edit.html', context={'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.summary = data['summary']
            issue.description = data['description']
            issue.status = data['status']
            issue.type = data['type']
            issue.save()
            return redirect('index')
        else:
            return render(request, 'issue/edit.html', context={'form': form, 'issue': issue})


class IssueDeleteView(View):

    def get(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        return render(request, 'issue/delete.html', context={'issue': issue})

    def post(self, request, *args, **kwargs):
        issue_pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=issue_pk)
        issue.delete()
        return redirect('index')


