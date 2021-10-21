install:
	pip install -r requirements.txt

run:
	uvicorn api.main:app --reload