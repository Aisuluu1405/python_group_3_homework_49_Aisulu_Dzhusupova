from datetime import datetime
from collections import deque
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
    redirect_url = ''
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
        self.object = get_object_or_404(self.model, pk=kwargs.get('pk'))
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
    confirm_deletion = True

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        if self.confirm_deletion:
            return render(request, self.template_name, context={self.context_key: object})
        else:
            try:
                object.delete()
                return redirect(self.get_redirect_url())
            except ProtectedError:
                return render(request, self.template)

    def post(self, request, *args, **kwargs):
        object = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            object.delete()
            return redirect(self.get_redirect_url())
        except ProtectedError:
            return render(request, self.template)


    def get_redirect_url(self):
        return self.redirect_url


class SessionUserMixin:
    page_times_visits = {}
    total_count = {
        'total': 0
    }
    all_time = 0
    page_duration_visits = {}
    date_buffer = deque()


    def save_in_session(self):                            #сохранили в сессию
        self.request.session['total_page_visits'] = self.page_times_visits
        self.request.session['total'] = self.total_count
        # print(self.page_times_visits)
        self.request.session['page_time_visits'] = self.page_duration_visits
        self.request.session['all_time'] = self.all_time
        # print(self.request.session['all_time'])


    def page_login(self):                   #как зашли на страницу пошел отсчет
        self.total_count['total'] += 1
        self.page_visit_count()
        self.save_in_session()
        self.get_total_time()
        date = datetime.now()
        self.date_buffer.append({self.request.path: date})

        if len(self.date_buffer) > 1:
            self.total_time()

    def set_request(self, request):
        self.request = request

    def get_total_time(self):    #общее время нахождения на страницах
        total_times = self.request.session['page_time_visits']
        for key, values in total_times.items():
            self.all_time += values
        # print(self.all_time)

    def total_time(self):  # время нахождения на странице
        f_date, s_date = self.date_buffer
        diff = list(s_date.values()).pop() - list(f_date.values()).pop()
        f_date_key = list(f_date.keys()).pop()
        if f_date_key in self.page_duration_visits.keys():
            self.page_duration_visits[f_date_key] += float(diff.total_seconds())
        elif f_date_key not in self.page_duration_visits.keys():
            self.page_duration_visits[f_date_key] = float(diff.total_seconds())
        self.date_buffer.popleft()
        # print(self.page_duration_visits)


    def page_visit_count(self):                    #счетчик страниц, определение страниц по path
        count = 1
        if self.request.path in self.page_times_visits.keys():
            self.page_times_visits[self.request.path] += 1
        elif self.request.path not in self.page_times_visits.keys():
            self.page_times_visits[self.request.path] = count
        # print(self.page_times_visits)


