{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

LICENSE: BSD
AUTHOR: {{cookiecutter.author_name}} ({{cookiecutter.author_email}})

CONFIGURATION
=============

{% if cookiecutter.use_env_for_configuration == 'yes' %}
The configuration comes from two sources:

local.cfg
---------

Which has basic supervisor/wsgi/nginx configuration for supervisor to build upon,
you NEED TO copy the local.cfg-dist to local.cfg first (non-versioned, local file)

ENV variables
-------------

django takes it's db settings from ENV variables

DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
DATABASE_HOST
DATABASE_PORT
{% else %}

local.cfg
---------

Which has all the basic supervisor/wsgi/nginx and database configuration for supervisor to build upon,
you NEED TO copy the `local.cfg-dist` to `local.cfg` first (non-versioned, local file)

{% endif %}

INSTALLATION
============

First time you NEED TO use either `make install` or `make install_prod`

We use makefile to run installation scripts:

    * make install_prod -> full installation, production environment (dependencies, config files, compass/bootstrap, db sync, migrations)
    * make install -> full installation, development environment (dependencies, config files, compass/bootstrap, db sync, migrations)
    * make prod -> partial installation, production environment (dependencies, config files)
    * make dev -> partial installation, development environment (dependencies, config files)


