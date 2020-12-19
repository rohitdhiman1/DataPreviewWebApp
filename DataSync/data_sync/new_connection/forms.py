from django.forms import ModelForm,NumberInput,IntegerField,PasswordInput,widgets,URLInput

from .models import NewConnection

class NewConnectionForm(ModelForm):
    class Meta:
        model = NewConnection
        fields = '__all__'
        widgets = {
            'password': PasswordInput(attrs={"type":"password"}),
            'port_number': NumberInput(attrs={"type": "number"})
        }
