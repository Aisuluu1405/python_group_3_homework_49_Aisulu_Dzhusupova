from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import TemplateView, View


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()


class DetailView(TemplateView):
    model = None
    context_key = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=kwargs.get('pk'))
        return context


class CreateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render (request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = self.model.objects.create(**form.cleaned_data)
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class EditView(View):
    model = None
    template_name = None
    form_class = None
    redirect_url = '/'
    context_key = 'object'

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        form = self.form_class(instance=object)
        return render(request, self.template_name, context={'form': form, self.context_key: object})


    def post(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        form = self.form_class(instance=object, data=request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = {'form': form, self.context_key: self.object}
        return render(self.template_name, context)

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    model = None
    template_name = None
    context_key = 'object'
    redirect_url = '/'
    template = None

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        return render(request, self.template_name, context={self.context_key: object})

    def post(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            object.delete()
            return redirect(self.get_redirect_url())
        except ProtectedError:
            return render(request, self.template)


    def get_redirect_url(self):
        return self.redirect_url

