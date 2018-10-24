#!/bin/bash

cd $(dirname ${0})
rm -rf apigee_python.egg-info/ build/ dist/
find . -name .ropeproject -type d | xargs rm -rf
find . -name "*.pyc" -type f | xargs rm -f
rm -rf build
rm -rf dist
rm -rf .pytest_cache
rm -rf .tox
rm -rf .eggs
rm test/pytestdebug.log
rm -rf docs/_build
