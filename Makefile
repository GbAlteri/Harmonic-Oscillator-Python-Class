
lint:
	black diatomic.py; flake8 diatomic.py; 

test:
	pytest -v test_diatomic.py

plot:
	python plot_diatomic.py