def can_finish_courses(total_courses, prerequisites):
    graph = {}
    for pair in prerequisites:
        if pair[1] not in graph:
            graph[pair[1]] = []
        graph[pair[1]].append(pair[0])

    def has_cycle(course, visited, stack):
        visited[course] = True
        stack[course] = True

        for neighbor in graph.get(course, []):
            if not visited[neighbor]:
                if has_cycle(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[course] = False
        return False

    visited = [False] * total_courses
    stack = [False] * total_courses

    for course in range(total_courses):
        if not visited[course]:
            if has_cycle(course, visited, stack):
                return False

    return True

total_courses = int(input("Give the number of courser:"))
number_of_prerequisites = int(input("Give the number of prerequisites"))

prerequisites = []
for _ in range(number_of_prerequisites):
    course_b,course_a = input("write the courser").split(",")
    prerequisites.append([course_a, course_b])

result = can_finish_courses(total_courses, prerequisites)

if result:
    print("It is possible to finish all courses.")
else:
    print("It is not possible to finish all courses due to prerequisites.")
