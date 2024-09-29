from django import forms
from starbucks.models import MainMenu

class MainMenuForm(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = "__all__"

class updateMenuForm(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = ('qty', 'name', )

class statusMenuForm(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = ('status', )