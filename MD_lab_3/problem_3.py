class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def count_rating(self, dist, src):
        k = 0
        for node in range(self.V):
            k += dist[node]
        return k - 19

    def minDistance(self, dist, sptSet):

        min = 1e7

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        sum = self.count_rating(dist, src)
        return sum

file_path = r'D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\matrix.txt'
matrix = []

with open(file_path, 'r') as file:
    names_line = file.readline().strip()
    names = names_line.split('|')
    for line in file:
        row = [value for value in line.split()]
        matrix.append(row)
raw_name_scores ={}
name_scores = {}
with open('D:\PSA_MD_LABS\PSA-MD_labs-main\PSA_lab_3\lab3files\influence.txt','r') as file:
    for line in file:
        name, score = line.strip().split(':')
        score = float(score)
        raw_name_scores[name] = score
name_scores = {key.strip(): value for key, value in raw_name_scores.items()}
matrix = [[int(value) for value in row[3:]] for row in matrix]


friends_count = [sum(row) for row in matrix]
most_friends_person_index = friends_count.index(max(friends_count))
name_count = dict(zip(names, friends_count))

print("--------------------------3.1----------------------------")
print(f"The person with the most friends is person {names[most_friends_person_index]} with {friends_count[most_friends_person_index]} friends.")
sorted_name_count = dict(sorted(name_count.items(), key=lambda item: item[1], reverse=True))

print("--------------------------3.2-----------------------------")
for name, count in sorted_name_count.items():
    print(f"{name.strip()} : {count} friends")
rating2 = []
g = Graph(20)
g.graph = matrix
for i in range(0,20):
    rating2.append(int(g.dijkstra(i)))

ratings = dict(zip(names,rating2))
sorted_ratings = sorted(ratings.items(), key=lambda item: item[1], reverse=True)

print("--------------------------3.3-----------------------------")
for person, rating in sorted_ratings:
    print(f"{person}: Rating {rating}")

new_rating = {}
print("--------------------------3.4-----------------------------")
for person in names:
    new_rating[person] = ratings[person] * name_scores[person.strip()] * 0.5

sorted_new_ratings = sorted(new_rating.items(), key=lambda item: item[1], reverse=True)
for person, rating in sorted_new_ratings:
    print(f"{person} : {rating} ")


