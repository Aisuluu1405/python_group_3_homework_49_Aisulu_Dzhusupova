from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View

from webapp.forms import IssueForm, StatusForm
from webapp.models import Issue, Status, Type


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
        template_name = 'issue_detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            issue_pk = kwargs.get('pk')
            context['issue'] = get_object_or_404(Issue, pk=issue_pk)
            return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue_add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                create=form.cleaned_data['create'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('detail', pk=issue.pk)
        else:
            return render(request, 'issue_add.html', context={'form': form})


def issue_edit_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'create': issue.create,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'issue_edit.html', context={'form': form, 'issue': issue})
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            issue.summary = data['summary']
            issue.description = data['description']
            issue.create = data['create']
            issue.status = data['status']
            issue.type = data['type']
            issue.save()
        return redirect('index')
    else:
        return render(request, 'issue_edit.html', context={'form': form, 'issue': issue})


def issue_delete_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        return render(request, 'issue_delete.html', context={'issue': issue})
    elif request.method == 'POST':
        issue.delete()
    return redirect('index')


class StatusIndexView(TemplateView):
    template_name = 'status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status_add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_index')
        else:
            return render(request, 'status_add.html', context={'form': form})


def status_edit_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'status_edit.html', context={'form': form, 'status': status})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            status.status = data['status']
            status.save()
        return redirect('status_index')
    else:
        return render(request, 'status_edit.html', context={'form': form, 'status': status})


def status_delete_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'status_delete.html', context={'status': status})
    elif request.method == 'POST':
        status.delete()
    return redirect('status_index')


class TypeIndexView(TemplateView):
    template_name = 'type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context
