.env:
	python3 -m venv .env
	./.env/bin/pip install pytest

test: .env
	./.env/bin/pytest tests.py
