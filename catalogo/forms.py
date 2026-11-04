from datetime import date

from django import forms

from .models import LugarPatrimonial


class LugarForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'imagen', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_anio_construccion(self):
        # Validación propia: el año no puede ser futuro ni demasiado antiguo
        anio = self.cleaned_data['anio_construccion']
        if anio < 1000 or anio > date.today().year:
            raise forms.ValidationError('Ingresa un año válido (entre 1000 y el año actual).')
        return anio
