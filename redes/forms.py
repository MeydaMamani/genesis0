from django import forms
from .models import Entity, Redes

class RedesForm(forms.ModelForm):
    class Meta:
        model = Redes
        fields = '__all__'
        widgets= {
            'state': forms.Select(attrs={
                'v-select2':'""',
                'class': 'form-control',
                'data-placeholder': 'Seleccione',
                'v-model': 'form.fields.state',
                'style':"width:100%"
            }),
        }