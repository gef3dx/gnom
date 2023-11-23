from django import forms
from .models import Tasks
from users.models import CustomUser


class TaskForm(forms.ModelForm):
    user = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['user'].choices = self.get_staff_users()

    def get_staff_users(self):
        staff_users = CustomUser.objects.filter(is_worker=True)
        user_choices = [(user.id, user.username) for user in staff_users]
        return user_choices

    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {"date": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', })}
        # exclude = ["author", "complectation", "sum_price_count", "remains"]