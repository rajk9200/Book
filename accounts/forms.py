from django import forms

from .models import Signup,UserProfile
class LoginForm(forms.Form):
    email1 = forms.EmailField()
    password1 =forms.CharField(max_length=100)


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Username Here'
            }
        )
    )
    #
    # email = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name','dob','city','pic','status')