from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View

from webapp.forms import IssueForm, StatusForm, TypeForm
from webapp.models import Issue, Status, Type
from django.db.models import ProtectedError


class IndexView(TemplateView):
    template_name = 'issue/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['issue'] = get_object_or_404(Issue, pk=issue_pk)
        return context


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


class StatusIndexView(TemplateView):
    template_name = 'status/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_index')
        else:
            return render(request, 'status/add.html', context={'form': form})


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


class TypeIndexView(TemplateView):
    template_name = 'type/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('type_index')
        else:
            return render(request, 'type/add.html', context={'form': form})


class TypeEditView(View):

    def get(self, request, *args, **kwargs):
        type_pk= kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'type': type.type,
            })
        return render(request, 'type/edit.html', context={'form': form, 'type':type})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        if form.is_valid():
            data = form.cleaned_data
            type.type = data['type']
            type.save()
            return redirect('type_index')
        else:
            return render(request, 'type/edit.html', context={'form': form, 'type': type})


class TypeDeleteView(View):

    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        return render(request, 'type/delete.html', context={'type': type})

    def post(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        try:
            type.delete()
            return redirect('type_index')
        except ProtectedError:
            return render(request, 'protected_error.html')
