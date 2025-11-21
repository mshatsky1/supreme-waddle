.PHONY: help run test clean

help:
	@echo "Available targets:"
	@echo "  run    - Run the main script"
	@echo "  test   - Run tests"
	@echo "  clean  - Clean generated files"

run:
	python main.py

test:
	@echo "No tests yet"

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

