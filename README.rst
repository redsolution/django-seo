==========
django-seo
==========

django-seo.

Installation:
=============

1. Put ``seo`` as LAST item to your ``INSTALLED_APPS`` in your ``settings.py`` within your django project.

2. Sync your database::

    ./manage.py syncdb

Usage:
======

In settings.py:
---------------

Add names of ModelAdmins to be override:: 
    SEO_FOR_MODELS = [
        '<app>.models.<Model>',
    ]

In template:
------------

First of all, load the seo_tags in every template you want to use it::

    {% load seo_tags %}
    
Use::
    {% show_seo <title|keywords|description> for <object> %}
    
Or::
    {% get_seo <title|keywords|description> for <object> as <variable> %}
    {{ <variable> }}

Example:
========

``settings.py``::
    INSTALLED_APPS = (
        ...
        'seo',
    )
    
    SEO_FOR_MODELS = [
        'item.models.Item',
    ]


``templates/object.html``::
    {% load seo_tags %}
    <html>
        <head>
            {% show_seo title for item %}
            {% show_seo keywords for item %}
            {% show_seo description for item %}
        </head>
        <body>
            {{ item.content }}
            {% get_seo title for item as seo_title %}
            <h1>{{ seo_title }}</h1>
        </body>
    </html>
