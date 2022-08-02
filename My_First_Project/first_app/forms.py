from django import forms
from first_app.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
