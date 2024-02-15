format:
	ruff format ./Algorithm ./DataStructure && isort ./Algorithm ./DataStructure

git_push:
	make format && git push
