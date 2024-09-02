from django import forms
from .models import Anuncio
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['local', 'preco', 'tipo_contrato', 'descricao', 'fotos']
        widgets = {
            'tipo_contrato': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields['local'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control'})
        self.fields['fotos'].widget.attrs.update({'class': 'form-control'})
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.enctype = 'multipart/form-data'
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-primary'))
