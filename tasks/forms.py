from django import forms
from .models import Tasks
from users.models import CustomUser


class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        widgets = {"date": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', })}
        exclude = ["complectation", "user", "date_create"]


class TaskExplanationsForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = "__all__"
        exclude = ["title", "description", "complectation", "status", "user", "date_create", "date"]