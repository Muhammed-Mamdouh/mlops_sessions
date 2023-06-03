install:
	pip install -r requirements.txt

lint:
	pylint hello.py

test:
	python -m pytest -vv test_hello.py
	python -m pytest -vv test_app.py