=====
Usage
=====

To use django-rest-hydra in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_rest_hydra.apps.DjangoRestHydraConfig',
        ...
    )

Add django-rest-hydra's URL patterns:

.. code-block:: python

    from django_rest_hydra import urls as django_rest_hydra_urls


    urlpatterns = [
        ...
        url(r'^', include(django_rest_hydra_urls)),
        ...
    ]
