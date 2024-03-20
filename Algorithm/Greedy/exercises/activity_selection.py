import typing as t


class Activity:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        return self.finish < other.finish

    def __repr__(self):
        return f"{self.name}: {self.start} - {self.finish}"


def sort_by_finish(activities: t.List[Activity]) -> t.List[Activity]:  # O(nlogn)
    return sorted(activities, key=lambda x: x.finish)


def best_selection(activities: t.List[Activity]) -> t.List[str]:  # O(nlogn)
    sorted_activities = sort_by_finish(activities)  # Sort by finish time O(nlogn)
    activities_to_do = [sorted_activities[0]]  # set the first activity name
    for activity in sorted_activities[1:]:  # O(n)
        if activities_to_do[-1].finish <= activity.start:
            activities_to_do.append(activity)
    return activities_to_do


activity1 = Activity("A1", 0, 6)
activity2 = Activity("A2", 3, 4)
activity3 = Activity("A3", 1, 2)
activity4 = Activity("A4", 5, 8)
activity5 = Activity("A5", 5, 7)
activities = [activity1, activity2, activity3, activity4, activity5]

print(best_selection(activities))
