# django-svg-tag

[![Build Status](https://travis-ci.org/bnzk/django-svg-tag.svg "Build Status")](https://travis-ci.org/bnzk/django-svg-tag/)
[![PyPi Version](https://img.shields.io/pypi/v/django-svg-tag.svg "PyPi Version")](https://pypi.python.org/pypi/django-svg-tag/)
[![Licence](https://img.shields.io/pypi/l/django-svg-tag.svg "Licence")](https://pypi.python.org/pypi/django-svg-tag/)

## Features

Output .svg files inline, with options how to treat them (cleanup, strip attributes, etc).

## Usage

Install with pip (not yet):

    pip install django-svg-tag
    
Add to installed apps:

    INSTALLED_APPS = [
    ...
    'svg_tag'
    ...
    ]
   
Place the svg files in your templates folder, for example in `your_project/svg/whatever.svg`.
Then use the tag in your template:

    {% load svg_tag %}
    {% svg_tag 'your_project/svg/whatever.svg' %}
    
svg_tag uses the django template engine to locate svg files.

## Development


### Getting started

- there is test app, available with `./manage.py runserver`.
- to run tests: ./manage.py test
- to run tests with django 1.11+: `tox` NOTYET


### Contributions

If you want to contribute to this project, please perform the following steps

    # Fork this repository
    # Clone your fork
    mkvirtualenv django-svg-tag
    pip install -r test_requirements.txt
    git checkout -b feature_branch
    # Implement your feature and tests
    git add . && git commit
    tox
    git push -u origin feature_branch
    # Send us a pull request for your feature branch