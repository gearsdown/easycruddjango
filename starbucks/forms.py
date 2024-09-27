from django import forms
from starbucks.models import MainMenu

class InsertNewMenu(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = "__all__"

class updateMenu(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = ('qty', 'name', )

class inActiveMenu(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = ('status', )