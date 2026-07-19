from django import forms
from .models import User


class EmployeeForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        ),
        required=False
    )

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "department",
            "role",
            "profile_image",
            "password"
        ]

        widgets = {

            "first_name":forms.TextInput(attrs={"class":"form-control"}),

            "last_name":forms.TextInput(attrs={"class":"form-control"}),

            "username":forms.TextInput(attrs={"class":"form-control"}),

            "email":forms.EmailInput(attrs={"class":"form-control"}),

            "phone":forms.TextInput(attrs={"class":"form-control"}),

            "department":forms.TextInput(attrs={"class":"form-control"}),

            "role":forms.Select(attrs={"class":"form-select"}),

            "profile_image":forms.ClearableFileInput(attrs={"class":"form-control"}),
        }