from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import TaskUser

class TaskUserLoginForm(AuthenticationForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
                field.label = ''
                field.errors = ''
            

class TaskUserRegisterForm(UserCreationForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'password1', 'password2', 'email', 'ava')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    