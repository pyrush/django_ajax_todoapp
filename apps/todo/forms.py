from django import forms
from .models import TODOModel


class TODOCreateForm(forms.ModelForm):
    class Meta:
        model = TODOModel
        fields = ['title']

    def clean_title(self):
        data = self.cleaned_data["title"]
        return data
