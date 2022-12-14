from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {
            'username': auth_forms.UsernameField,
        }
        # Does not work for password1 and password2
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
        # }


class UserLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'email',
            'profile_picture': 'Image URL',
            'gender': 'Gender',
        }


class UserDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def __hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    class Meta:
        model = UserModel
        fields = ()
