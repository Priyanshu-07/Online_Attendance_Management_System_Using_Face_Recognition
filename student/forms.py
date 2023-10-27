from django import forms
from .models import stud


class studform(forms.ModelForm):
    class Meta:
        model = stud
        fields = ('roll_no', 'stud_image')
