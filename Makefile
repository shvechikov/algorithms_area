.env:
	python3 -m venv .env
	./.env/bin/pip install pytest

test: .env
	./.env/bin/pytest --duration=20 tests.py
