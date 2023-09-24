from django import forms
from .models import Task
from multiupload.fields import MultiFileField


class MultiFileInput(forms.FileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs={'multiple': True})

class TaskForm(forms.ModelForm):

    photos = MultiFileField(min_num=1, max_num=5, max_file_size=1024*1024*5)
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_completed']
