# Django SEO application


Open source SEO management system based on the Django framework

## Features
- Easy SEO fields attachment to any site page
- Several ways to render seo-fields
- Query caching for faster page loading

## Requirements
- Django 1.11.*
- Python 2.7

## Installation and basic usage

1. Install package:

    `` pip install git+git://github.com/oldroute/django-seo.git``

2. Configure your settings file:

	**SEO_FOR_MODELS** - list of models for attaching seo-fields in format: <app_name>.<model_name>.

	Simple settings configuration:

    ```python
    INSTALLED_APPS += ['seo']
    SEO_FOR_MODELS = [
        'pages.Page',
        'easy_news.News',
    ]
    ```

3. Call template tag in html template:

  	**Use case 1**: Call for specified url. In this case you must fill seo fields for specified url address in the admin of seo application.

    ```html
	<head>
        ...
        {% seo %}
        ...
    </head>
    ```

  	**Use case 2**: Call for specified object (model instance declared in **SEO_FOR_MODELS**). In this case you must fill seo fields in the admin page of the object:

    ```html
	<head>
        ...
        {% seo object %}
        ...
    </head>
    ```

4. Apply migrations and run local server:

    ```python
    python manage.py migrate seo
    python manage.py runserver
    ```
5. Fill seo-fields in admin interface

**Configure is done!**

## Advanced template tag usage

**Use case 3**: Setting default values for fields through parameters: ``title_default``, ``desc_default``, ``keys_default``:

```html
<head>
...
{% seo current_page title_default='My title' %}
...
</head>
```


**Use case 4**: Setting text postfix through parameters: ``title_postfix``, ``desc_postfix``, ``keys_postfix``:


```html
<head>
...
{% seo current_page title_postfix=' my postfix' %}
...
</head>
```

Your can combine any parameters together