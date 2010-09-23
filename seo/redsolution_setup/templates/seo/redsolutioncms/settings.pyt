# ------------  django-seo ----------------
INSTALLED_APPS += ['seo']

SEO_FOR_MODELS = [{% for model in seo_settings.models.all %}
    '{{ model.model }}',{% endfor %}
]
