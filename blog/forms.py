from django import forms
from django.forms import ModelForm, Select, ModelChoiceField
from .models import Blog, Category


class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        category = forms.ChoiceField(widget=forms.Select(),
                              required=True)

# category = forms.ModelChoiceField(queryset=Category.objects.all())

# class Category(forms.ModelForm):
#     class Meta:
#         model = Category
#         widgets = { 'name': Select() }
# class MatchForm(forms.Form):
#     category = forms.ChoiceField(choices = [])

#     def __init__(self, *args, **kwargs):
#         super(MatchForm, self).__init__(*args, **kwargs)
#         self.fields['category'].choices = [(x.pk, x.get_name()) for x in Category.objects.all()]

#email = forms.EmailField()
# fiels = forms.FileField()
# url = forms.URLField()
# words = forms.CharField(max_length = 200)
# max_number = forms.ChoiceField(choices=[{'1','one'}, {'2','two'},{'3','three'}])