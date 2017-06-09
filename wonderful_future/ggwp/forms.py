from django import forms
from ggwp.models import Category,Page,UserProfile
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapUneditableInput

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text='Please enter category name!')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0,)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Category
        fields = ('name',)

class PagesForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text="Please enter page title!")
    url = forms.CharField(max_length=200,help_text='Please enter the Url of zhe page!')
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = Page
        exclude = ('category',)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            print url
        return cleaned_data
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')

