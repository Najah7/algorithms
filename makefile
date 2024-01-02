FILE ?= $(shell find . -name "*.py")

format:
	black $(FILE) && isort $(FILE)

git_push:
	make format && git push
