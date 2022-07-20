.PHONY: help
.DEFAULT_GOAL := help

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build:
	@echo "--> Building base image"
	docker build -t rekognition -f docker/app/Dockerfile .
	@echo "--> Building Compose"
	docker-compose build

build-no-cache:
	@echo "--> Building base image"
	docker build -t rekognition -f docker/app/Dockerfile . --no-cache
	@echo "--> Building Compose"
	docker-compose build

test:
	@echo "--> Testing on Docker."
	docker-compose run app pytest $(path) -s --cov-report term-missing --cov-fail-under 100

bash:
	docker-compose run app bash

delete-requirements:
	@echo "--> Deleting old requirements files"
	cd requirements && \
	rm -f dev.txt && \
	rm -f test.txt

compile-requirements: delete-requirements
	@echo "--> Compiling requirements"
	docker-compose run app bash -c	" \
	cd requirements && \
	pip-compile dev.in && \
	pip-compile test.in "

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 rekognition tests

coverage: ## check code coverage quickly with the default Python
	coverage run --source rekognition -m pytest

install: clean ## install the package to the active Python's site-packages
	python setup.py install

install-requirements: ## installs requirements locally
	pip install -r requirements/dev.txt
	pip install -r requirements/test.txt
