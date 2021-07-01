from django.forms import ModelForm
from .models import Keys

class KeysForm(ModelForm):
    class Meta:
        model = Keys
        fields=['keys','docfile']

   

   

      
