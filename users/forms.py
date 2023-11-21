from django.contrib.auth.forms import  AuthenticationForm, UsernameField
from django import forms

class loginForm(AuthenticationForm):
     
     

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields.pop('username')
          self.fields['email'].lable = 'Email'

          email = forms.EmailField(
               label='Email',
               max_length=254,
               widget=forms.EmailInput(attrs={"autofocus": True}),
          )

          password = forms.CharField(
               label='Password',
               strip=False,
               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
          )
         