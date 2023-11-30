from django import forms
from .models import Tasks
from users.models import CustomUser


class TaskForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role="Сотрудник"), label="Выберите сотрудника")

    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {"date": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', })}
        # exclude = ["author", "complectation", "sum_price_count", "remains"]


class TaskExplanationsForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = "__all__"
        exclude = ["title", "description", "complectation", "status", "user", "date_create", "date"]