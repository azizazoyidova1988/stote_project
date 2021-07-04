from django import forms
from .models import *


class CommenterForm(forms.ModelForm):
    class Meta:
        model = Commenter()
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects()
        fields = '__all__'


class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams()
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial()
        fields = '__all__'



class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = '__all__'


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services()
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = '__all__'