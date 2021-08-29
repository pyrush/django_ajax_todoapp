from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import TODOModel
from .forms import TODOCreateForm


class TODOView(CreateView):
    model = TODOModel
    fields = ['title']

    def post(self, request, *args, **kwargs):
        form = TODOCreateForm(self.request.POST)
        if form.is_valid():
            new_task = form.save()
            redirect_url = self.request.POST.get("redirectInput")
            if redirect_url:
                return redirect(f'todo:{redirect_url}')
            return redirect('todo:task_list_url')


class TODOListView(ListView):
    model = TODOModel
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TODOCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TODOCreateForm(self.request.POST)
        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)
        else:
            return redirect("task:task_list_url")
