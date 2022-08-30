from django.forms import ModelForm
from .models import trainerLogin

class trainerLoginForm(ModelForm):
    class Meta:
        model = trainerLogin
        labels = {
            "trainerUserName": "Trainerize Email Address",
            "trainerPassword": "Trainerize Password"
        }
        fields = '__all__'

        