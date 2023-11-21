from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {"date": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', })}
        # exclude = ["author", "complectation", "sum_price_count", "remains"]