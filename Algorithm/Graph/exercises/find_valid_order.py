import typing as t

Graph = t.Dict[str, t.List[str]]


def create_project_graph(tasks: str, dependencies: t.List[t.Tuple[str, str]]) -> Graph:
    project_graph = {}
    for project in tasks:
        project_graph[project] = []
    for pre_req_task, task in dependencies:
        project_graph[pre_req_task].append(task)
    return project_graph


tasks = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]


def get_dependent_tasks(project: Graph) -> t.Set[str]:
    dependent_tasks = set()
    for task in project:
        dependencies = project[task]
        if len(dependencies) > 0:
            [dependent_tasks.add(task) for task in dependencies]
    return dependent_tasks


def get_independent_tasks(dependent_tasks: t.Set[str], project: Graph) -> t.Set[str]:
    independent_tasks = set()
    for task in project:
        if task not in dependent_tasks:
            independent_tasks.add(task)
    return independent_tasks


def find_valid_order(
    tasks: str, dependencies: t.List[t.Tuple[str, str]]
) -> t.List[str]:
    valid_order = []
    project = create_project_graph(tasks, dependencies)
    while project:
        dependent_tasks = get_dependent_tasks(project)
        independent_tasks = get_independent_tasks(dependent_tasks, project)
        if (
            len(independent_tasks) == 0 and project
        ):  # when there are no tasks which can be done independently and project is not completed yet
            raise Exception("There is a cycle in the dependencies")
        for task in independent_tasks:
            valid_order.append(task)
            del project[task]
    return valid_order


graph = create_project_graph(tasks, dependencies)
print(get_dependent_tasks(graph))
print(get_independent_tasks(get_dependent_tasks(graph), tasks))
print(find_valid_order(tasks, dependencies))
