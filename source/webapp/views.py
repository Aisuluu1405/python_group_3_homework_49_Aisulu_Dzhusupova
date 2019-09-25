from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

# from webapp.forms import IssueForm
from webapp.models import Issue


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

