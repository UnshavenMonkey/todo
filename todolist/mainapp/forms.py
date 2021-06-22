from django.forms import ModelForm, fields

from .models import Utask

class UtaskForm(ModelForm):
    class Meta:
        model = Utask
        fields = ('title', 'category')