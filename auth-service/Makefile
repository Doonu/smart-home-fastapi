.DEFAULT_GOAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

run:
	poetry run uvicorn main:app --host $(HOST) --port $(PORT) --reload

install:
	@echo "Подтягиваем зависимость $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall:
	@echo "Удаляем зависимость $(LIBRARY)"
	poetry remove $(LIBRARY)