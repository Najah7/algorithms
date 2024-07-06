fmt:
	ruff format ./Algorithm ./DataStructure && isort ./Algorithm ./DataStructure

git_push:
	make fmt && git push
