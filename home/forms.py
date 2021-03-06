from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User
    
    username = forms.CharField(label='',
        widget=forms.TextInput(attrs=
        {
            'placeholder':'Username',
            'class': 'special-input'
        }))
    email = forms.CharField(label='',
        widget=forms.EmailInput(attrs=
        {
            'placeholder': 'Email',
            'class': 'special-input'
        }))
    
    password1 = forms.CharField(label='',
        widget=forms.PasswordInput(attrs=
        {
            'placeholder': 'Password',
            'class': 'special-input'
        }))
    password2 = forms.CharField(label='',
        widget=forms.PasswordInput(attrs=
        {
            'placeholder': 'Confirm Password',
            'class': 'special-input'
        }))
    


