class Solution:
    def canFinish(self,n: int, p: List[List[int]]) -> bool:
        d = {i: [] for i in range(n)}
        for prereq in p:
            d[prereq[0]].append(prereq[1])
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not d[course]:
                return True
            visited.add(course)
            for prereq in d[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            d[course] = []
            return True
        for i in range(n):
            if not dfs(i):
                return False
        return True