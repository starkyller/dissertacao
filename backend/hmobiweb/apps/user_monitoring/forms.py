from django import forms

from django_json_widget.widgets import JSONEditorWidget

from .models import CollectedData


class CollectedDataForm(forms.ModelForm):

    class Meta:
        model = CollectedData
        fields = '__all__'
        widgets = {
            'dataSample': JSONEditorWidget,
        }