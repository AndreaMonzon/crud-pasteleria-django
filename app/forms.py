from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))

    class Meta:
        # para traer los datos del modelo de contacto
        model = Contacto
    # field son los campos del formulario ,que deben estar en el modelo
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
    # para traer todos los campos del modelo  fields = '__all__'


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[
                              MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=150000)
# para validar que elnombre del producto ya existe

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")

        return nombre

    class Meta:
        # para traer los datos del modelo de contacto
        model = Producto
    # field son los campos del formulario ,que deben estar en el modelo

    # para traer todos los campos del modelo  fields = '__all__'
        fields = '__all__'

# heredo del formulario de django que ya existe


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
