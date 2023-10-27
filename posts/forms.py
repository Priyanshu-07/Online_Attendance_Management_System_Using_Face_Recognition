from django import forms
from .models import Post, category

choice = category.objects.all().values_list('name', 'name')

choice_list = []

for item in choice:
    choice_list.append(item)


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'category', 'header_image',)  # 'author' 

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control form-box ', 'placeholder': "Title"}),
            'title-tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices = choice_list , attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Editform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title-tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
