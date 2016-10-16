#!/usr/bin/env bash
source ../venv/bin/activate
python manage.py dumpdata --indent 2 -e contenttypes -e sessions -e auth -e admin > assets/fixtures/data.json