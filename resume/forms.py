from django import forms
from .models import ResumeDetails
class Book(ModelForm):
    class Meta:
        model = ResumeDetails
        fields = '__all__'