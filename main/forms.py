# main/forms.py
from django import forms
from .models import BlogPost, Product
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Version


class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_WORDS:
            if word in name:
                raise ValidationError('Недопустимое слово в названии продукта')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_WORDS:
            if word in description:
                raise ValidationError('Недопустимое слово в описании продукта')
        return description


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview', 'is_published')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Имя должно быть не менее 3 символов.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Пожалуйста, используйте действительный адрес электронной почты из example.com")
        return email
