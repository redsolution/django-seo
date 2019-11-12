from django.apps import apps as django_apps


def importpath(path, error_text=None):

    app_label, model_name = tuple(path.split('.'))
    return django_apps.get_model(app_label, model_name)
