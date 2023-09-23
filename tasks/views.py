from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from django.core.exceptions import PermissionDenied
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this task.")
        return task

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_details.html'
    context_object_name = 'task'
    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this task.")
        return task

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        return task

# REST API VIEWS

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]