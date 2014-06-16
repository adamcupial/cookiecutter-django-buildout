.DEFAULT_GOAL = usage
.PHONY = prod dev clean dist install install_prod

usage:
	@echo
	@echo "  .: powered by https://github.com/onjin/django-buildout-template :."
	@echo
	@echo "  .: Project builder usage :."
	@echo
	@echo "  dev            - build development version, no crontabs"
	@echo "  prod           - build production version with crontabs"
	@echo
	@echo "  clean          - rm py[co] files"
	@echo "  dist           - !!! rm eggs, parts, downloads, bootstrap.py"
	@echo "  compile        - compile .py files"
	@echo

system:
	@mkdir -p ~/logs
	@mkdir -p var/log
	@mkdir -p downloads
	@mkdir -p eggs
	@mkdir -p parts
	@mkdir -p develop-eggs
	@mkdir -p project_static


bootstrap.py :
	wget http://downloads.buildout.org/2/bootstrap.py
	python -S bootstrap.py

bin/buildout : bootstrap.py
	@mkdir -p etc
	@mkdir -p var/log

dev: system bin/buildout compile
	bin/buildout -c dev.cfg
	@echo
	@echo " .: DEVELOPMENT configuration was built, so NO CRON here"
	@echo

prod: system bin/buildout compile
	bin/buildout -c prod.cfg
	@echo
	@echo " .: PRODUCTION configuration was built, with CRON installed"
	@echo


clean:
	find . -name '*.py[oc~]'| xargs rm -f

dist: clean
	rm -rf bin develop-eggs eggs parts .installed.cfg downloads bootstrap.py

compile:
	python -c 'import compileall;  compileall.compile_dir("./{{ cookiecutter.project_name }}/", force=True, quiet=True);'

install: dev
{% if cookiecutter.use_compass == 'yes' %}
	bin/compass create -s expanded {% if cookiecutter.use_bootstrap == 'yes' %}-r bootstrap-sass --using bootstrap{% else %}--bare{% endif %} --sass-dir=sass --css-dir project_static/css --javascripts-dir project_static/js --fonts-dir project_static/fonts --images-dir project_static/images --no-line-comments --relative-assets
{% endif %}
	bin/django syncdb
{% if cookiecutter.migration_engine == 'south' %}
	bin/django migrate
{% endif %}

install_prod: prod
{% if cookiecutter.use_compass == 'yes' %}
	bin/compass create -s expanded {% if cookiecutter.use_bootstrap == 'yes' %}-r bootstrap-sass --using bootstrap{% else %}--bare{% endif %} --sass-dir=sass --css-dir project_static/css --javascripts-dir project_static/js --fonts-dir project_static/fonts --images-dir project_static/images --no-line-comments --relative-assets
{% endif %}
	bin/django syncdb
{% if cookiecutter.migration_engine == 'south' %}
	bin/django migrate
{% endif %}
