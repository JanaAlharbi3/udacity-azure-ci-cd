install:
	python3 -m pip install --upgrade pip setuptools wheel
	python3 -m pip install --only-binary=:all: -r requirements.txt

test:
	python3 -m pytest -vv

lint:
	pylint --disable=R,C hello.py

all: install lint test
