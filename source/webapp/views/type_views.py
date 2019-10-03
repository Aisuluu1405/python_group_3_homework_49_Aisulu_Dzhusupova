from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View

from webapp.forms import TypeForm
from webapp.models import Type
from django.db.models import ProtectedError


class TypeIndexView(ListView):
    template_name = 'type/index.html'
    context_object_name = 'types'
    model = Type


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
