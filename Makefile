install:
	pip install -r requirements.txt

run:
	uvicorn api.main:app --reload

pylint:
	pylint -j`nproc` api
