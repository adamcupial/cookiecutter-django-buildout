cookiecutter-django-buildout
============================

django with buildout template skeleton based on cookiecutter

Author:
=======

Adam Cupiał

Installation:
=============

1. Install cookiecutter (https://github.com/audreyr/cookiecutter)

.. code-block:: bash

    $ pip install cookiecutter

2. build the template

.. code-block:: bash

    $ cookiecutter https://github.com/adamcupial/cookiecutter-django-buildout

3. go to your project's directory and read README.rst file


Settings:
==========

  * project_name, default: 'project'
  * repo_name, default:'project_repository'
  * author_name, default: 'Joe Doe'
  * author_email, default: 'noone@nowhere.com'
  * description, default: 'Short description of the project'
  * migration_engine, default:'south', one of 'south', 'none'
  * admin_engine, default: 'grappelli', one of 'grappelli', 'default', 'none'
  * django_version, default: '1.6'
  * database_engine, default: 'sqlite', one of 'sqlite', 'postgres', 'mysql'
  * use_env_for_configuration, default: 'yes'
  * use_compass, default: 'yes'
  * use_bootstrap, default: 'yes'

Aknowledgements:
================

This tool is based on Cookiecutter (https://github.com/audreyr/cookiecutter) and django-buildout-template (https://github.com/onjin/django-buildout-template)
