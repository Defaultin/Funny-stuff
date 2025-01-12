"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, for pair [0, 1], to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Also return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Examples:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0.
So the correct course order is [0,1].

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take.
To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3].
Another correct ordering is [0,2,1,3].

Input: numCourses = 1, prerequisites = []
Output: [0]
"""


def resolve(courses: int, prereqs: list[list[int]]) -> tuple[bool, list[int]]:
    order = []
    state = [0] * courses  # 0 = unvisited, 1 = visiting, 2 = visited
    graph = [[] for _ in range(courses)]
    for a, b in prereqs:
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
        order.append(course)
        return True

    for course in range(courses):
        if state[course] == 0:  # unvisited
            if not dfs(course):
                return False, []

    return True, order[::-1]


if __name__ == "__main__":
    print(resolve(2, [[1, 0]]))
    print(resolve(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(resolve(1, []))
