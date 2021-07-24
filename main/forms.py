from django.forms import ModelForm, fields
from .models  import Applicants

class ApplicationForm(ModelForm):
    class Meta:
        model = Applicants
        fields = '__all__'