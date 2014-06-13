cookiecutter-django-buildout
============================

django with buildout template skeleton based on cookiecutter

Installation:
=============

 1. Install cookiecutter (https://github.com/audreyr/cookiecutter)

    pip install cookiecutter

 2. build the template

    cookiecutter https://github.com/adamcupial/cookiecutter-django-buildout

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
  * database_name, default: ''
  * database_user, default: ''
  * database_password, default: ''
  * database_host, default: ''
  * database_port, default: ''
