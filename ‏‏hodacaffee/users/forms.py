from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='اسم المستخدم',
        min_length=4,
        max_length=150,
        help_text='مطلوب. 4-150 حرف. يمكن استخدام الحروف والأرقام و @ . + - _ فقط.',
        error_messages={
            'required': 'يجب إدخال اسم المستخدم',
            'min_length': 'يجب أن يكون اسم المستخدم 4 أحرف على الأقل',
            'max_length': 'يجب أن لا يتجاوز اسم المستخدم 150 حرف',
            'unique': 'اسم المستخدم مستخدم بالفعل'
        }
    )
    
    email = forms.EmailField(
        label='البريد الإلكتروني',
        required=True,
        help_text='مطلوب. أدخل عنوان بريد إلكتروني صالح.',
        error_messages={
            'required': 'يجب إدخال البريد الإلكتروني',
            'invalid': 'يرجى إدخال عنوان بريد إلكتروني صالح'
        }
    )

    password1 = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput,
        help_text='كلمة المرور يجب أن تكون 8 أحرف على الأقل وتحتوي على أحرف وأرقام',
        error_messages={
            'required': 'يجب إدخال كلمة المرور'
        }
    )

    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput,
        help_text='أدخل نفس كلمة المرور مرة أخرى للتأكيد',
        error_messages={
            'required': 'يجب تأكيد كلمة المرور'
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('اسم المستخدم مستخدم بالفعل')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('البريد الإلكتروني مستخدم بالفعل')
        return email
