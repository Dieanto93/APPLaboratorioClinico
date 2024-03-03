from django import forms
from .models import Paciente , Resultado_examen, Examen_disponible, Pedido_examen

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['cedula','nombre', 'edad', 'direccion']


class ResultadoExamenForm(forms.ModelForm):
    class Meta:
        model = Resultado_examen
        fields = ['valor_resultado', 'rango']

class SeleccionarExamenesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        examenes = kwargs.pop('examenes')
        super(SeleccionarExamenesForm, self).__init__(*args, **kwargs)
        for examen in examenes:
            self.fields[str(examen.id)] = forms.BooleanField(label=examen.nombre_examen, required=False)

class PedidoExamenForm(forms.ModelForm):
    class Meta:
        model = Pedido_examen
        fields = ['paciente']
