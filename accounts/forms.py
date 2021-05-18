from django import forms
from .models import Profile
from pin.models import Pin, Board


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3','rows':3}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'photo', 'age', 'bio')


class PinForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    board = forms.ModelChoiceField(queryset=Board.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    caption = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-3','rows':3}))

    class Meta:
        model = Pin
        fields = ('title','board','image','url','caption')


class BoardForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3','rows':3}))

    class Meta:
        model = Board
        fields = ('title','description',)