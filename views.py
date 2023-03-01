from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm
from authentication.serializers import RegisterSerializer
from rest_framework import serializers

def task_create(request):
     if request.method == "POST":
         form = TaskForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect(reverse("tasks:task_list"))
     else:
         form = TaskForm()

     return render(request, "tasks/task_form.html", { "form": form, })

def task_list(request):
     tasks = Task.objects.all()
     return render(request, "tasks/task_list.html", { "tasks": tasks,})

def task_detail(request, pk):
     task = get_object_or_404(Task, pk=pk)
     return render(request, "tasks/task_detail.html", { "task": task, })


class SimpleLoginView(LoginView):
    template_name = 'signin.html'


class SignupView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('authentication:signin')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next')
        if next_url:
            self.success_url = next_url
        return response

class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'