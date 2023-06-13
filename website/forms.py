from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Direccion Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['username'].widget.label = ''
        self.fields['username'].widget.help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Solo letras y dígitos @/./+/-/_ .</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].widget.label = ''
        self.fields['password1'].widget.help_text = '<ul class="form-text text-muted small"><li>La contraseña no puede ser similar a su nombre.</li><li>La contraseña debe contar con al menos 8 caracteres.</li><li>La contraseña no puede ser un término común.</li><li>La contraseña no puede ser solo números.</li></ul>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password1'].widget.label = ''
        self.fields['password1'].widget.help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que la casilla anterior.</small></span>'

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Apellidos", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Teléfono", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Distrito", "class":"form-control"}), label="")
    province = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Provincia", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Código", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)

  