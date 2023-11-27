from django import forms
from .models import Product, Complectation, ProductSmeta, Provider, GroupProduct, Receipts, ServiceSmeta

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


# from users.models import CustomUser

# class CustomUserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields =  ["email", "username", "first_name", "last_name", "password1", "password2"]

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "phone", "first_name", "last_name", "role", "is_staff")
        
        
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "phone", "first_name", "last_name", "role", "is_staff")


class ComplectationForm(forms.ModelForm):
    class Meta:
        model = Complectation
        fields = "__all__"
        exclude = ["date_create", "author", "balance", "procent"]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {"date_order": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', }), "date_shipment": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date',})}
        exclude = ["author", "complectation", "sum_price_count", "remains"]

class ProductSmetaForm(forms.ModelForm):

    class Meta:
        model = ProductSmeta
        fields = "__all__"
        widgets = {"date_create": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', }),}
        exclude = ["author", "complectation"]

class ReceiptsForm(forms.ModelForm):

    class Meta:
        model = Receipts
        fields = "__all__"
        widgets = {"date_create": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', }),}
        exclude = ["author", "complectation"]

class ServiceSmetaForm(forms.ModelForm):

    class Meta:
        model = ServiceSmeta
        fields = "__all__"
        widgets = {"date_create": forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', }),}
        exclude = ["author", "complectation", "price_all", "price_procent"]

class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = "__all__"

class GroupProductForm(forms.ModelForm):

    class Meta:
        model = GroupProduct
        fields = "__all__"