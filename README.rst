=============================
django-rest-hydra
=============================

.. image:: https://badge.fury.io/py/django-rest-hydra.svg
    :target: https://badge.fury.io/py/django-rest-hydra

.. image:: https://travis-ci.org/invinciblycool/django-rest-hydra.svg?branch=master
    :target: https://travis-ci.org/invinciblycool/django-rest-hydra

.. image:: https://codecov.io/gh/invinciblycool/django-rest-hydra/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/invinciblycool/django-rest-hydra

Django Port of Hydrus

Documentation
-------------

Full documentation can be found at https://django-rest-hydra.readthedocs.io.

Quickstart
----------

Install django-rest-hydra::

    pip install django-rest-hydra

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
