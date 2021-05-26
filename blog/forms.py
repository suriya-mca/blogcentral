from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','content','status')
        widgets = {
            'content' : SummernoteWidget(),
        }

class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())