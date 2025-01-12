"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, for pair [0, 1], to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Examples:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1.
So it is impossible.
"""


def can_finish(courses: int, prerequisites: list[list[int]]) -> bool:
    state = [0] * courses  # 0 = unvisited, 1 = visiting, 2 = visited
    graph = [[] for _ in range(courses)]
    for a, b in prerequisites:
        graph[b].append(a)

    def dfs(course: int) -> bool:
        if state[course] == 1:  # visiting, found a cycle
            return False
        if state[course] == 2:  # visited, no cycle here
            return True

        state[course] = 1  # visiting

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        state[course] = 2  # visited
        return True

    for course in range(courses):
        if state[course] == 0:  # unvisited
            if not dfs(course):
                return False

    return True


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
    print(can_finish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    print(can_finish(3, [[1, 0], [2, 1], [0, 2]]))
    print(can_finish(4, [[1, 0], [2, 1], [3, 2]]))
