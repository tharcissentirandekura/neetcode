class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build grad
        graph = self.buildGraph(numCourses, prerequisites)
        
        indegree = [0] * numCourses # calculate indegree
        for course, prereq in prerequisites:
            indegree[course] += 1
        
        # traverse
        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course) # start with the course that doesn't have prereq first
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1 # we take one prereq
                if indegree[next_course] == 0:
                    queue.append(next_course) # add the course with no prereq
        if len(res) != numCourses:
            return []
        return res


    def buildGraph(self,numCourses,prerequisites):
        graph = {course: [] for course in range(numCourses)}
        for course,prereq in prerequisites:
            graph[prereq].append(course)
        return graph





