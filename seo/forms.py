from django import forms
from seo.models import Seo

class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo

    title = forms.CharField(
        required=not Seo._meta.get_field('title').blank,
        widget=forms.Textarea(attrs={'cols': '120', 'rows': '2'}),
        label=Seo._meta.get_field('title').verbose_name,
        initial=Seo._meta.get_field('title').default,
        help_text=Seo._meta.get_field('title').help_text,
        max_length=Seo._meta.get_field('title').max_length,
    )
    description = forms.CharField(
        required=not Seo._meta.get_field('description').blank,
        widget=forms.Textarea(attrs={'cols': '120', 'rows': '2'}),
        label=Seo._meta.get_field('description').verbose_name,
        initial=Seo._meta.get_field('description').default,
        help_text=Seo._meta.get_field('description').help_text,
        max_length=Seo._meta.get_field('description').max_length,
    )
    keywords = forms.CharField(
        required=not Seo._meta.get_field('keywords').blank,
        widget=forms.Textarea(attrs={'cols': '120', 'rows': '5'}),
        label=Seo._meta.get_field('keywords').verbose_name,
        initial=Seo._meta.get_field('keywords').default,
        help_text=Seo._meta.get_field('keywords').help_text,
        max_length=Seo._meta.get_field('keywords').max_length,
    )
