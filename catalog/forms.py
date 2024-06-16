from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Name contains forbidden word: {word}")
        return name

    def cleaned_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError(f"Description contains forbidden word: {word}")
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']

    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        product = self.cleaned_data['product']
        if is_active and product.versions.filter(is_active=True).exists():
            raise forms.ValidationError("Active version already exists")
        return is_active


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'is_published', 'description')