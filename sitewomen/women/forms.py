from django import forms
from .models import Category, Husband, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Категория не выбрана',
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        required=False,
        label='Муж',
        empty_label='Не замужем',
    )    

    class Meta:
        model = Women
        fields = ("title", "slug", "content", "is_published", "cat", "husband", "tags")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 5})
        }
        labels = {
            "slug": "URL"
        }
        
    
    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) > 50:
            raise ValidationError("Заголовок не может быть более 50 символов")
        
        return title
    