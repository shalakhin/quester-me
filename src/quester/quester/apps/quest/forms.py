from django import forms
from quest.models import Quest

class QuestForm(forms.ModelForm):

    class Meta:
        model = Quest
        fields = ('name', 'description', 'type', 'difficulty_level')

        widgets = {
            'type': forms.HiddenInput(),
        }





