from django import forms

from django_json_widget.widgets import JSONEditorWidget

from .models import Solution


class SolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
        fields = '__all__'
        widgets = {
            'sampleJsonSchema': JSONEditorWidget,
        }