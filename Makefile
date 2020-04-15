usage:
	@echo Usage: make [$$(cat Makefile | grep -vPe '^\t|^\.|^$$' | sed 's/:$$//g' | paste -sd "|" -)]

test:
	flake8
	pytest

watch:
	pytest-watch --beforerun='echo "Flake 8: " && flake8 ; echo "Pytest:"'

publish: dist | test
	twine upload dist/*

dist: README.md *.py mocktail
	rm -rf dist
	python setup.py sdist

.PHONY: usage test watch publish
