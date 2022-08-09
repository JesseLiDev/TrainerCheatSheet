from django.forms import ModelForm
from .models import trainerLogin

class trainerLoginForm(ModelForm):
    class Meta:
        model = trainerLogin
        fields = '__all__'

        