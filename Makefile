install:
	python -m pip install -r requirements.txt

dev-run:
	uvicorn main:app --reload

run:
	uvicorn main:app --host 0.0.0.0 --port 80

freeze:
	pip freeze > requirements.txt

test:
	python -m unittest
