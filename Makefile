all: lint test

lint:
	black real_world tests
	isort -rc real_world tests
	flake8 real_world
	mypy real_world

test:
	pytest tests --cov=real_world

.PHONY: all lint test
