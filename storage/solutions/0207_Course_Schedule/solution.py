class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for pre in graph[course]:

                if not dfs(pre):
                    return False

            visiting.remove(course)

            visited.add(course)

            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True