from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號') 
    password = forms.CharField(label='密碼', widget=forms.PasswordInput()) 
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput()) 
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user