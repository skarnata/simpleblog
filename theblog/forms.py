from django import forms

from .models import Post, Category

"""
Widget untuk Dropdown adalah Select
"""
choice = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choice:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title tag'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        }
