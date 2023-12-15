def find_cheapest_price(n, flights, start, destination, k):
    graph = {}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    heap = [(0, start, k + 1)]
    
    while heap:
        cost, current, stops = min(heap, key=lambda x: x[0])
        heap.remove((cost, current, stops)) 

        if current == destination:
            return cost

        if stops > 0:
            if current in graph:
                for neighbor, price in graph[current]:
                    heap.append((cost + price, neighbor, stops - 1))

    return "no route"


n = int(input("Enter the number of cities: "))
flights = []    
for _ in range(n):
    flight_info = list(map(int, input("Enter flight [from,to,price]: ").split()))
    flights.append(flight_info)

start = int(input("Enter the starting city: "))
destination = int(input("Enter the destination city: "))
k = int(input("Enter the maximum number of stops allowed: "))


result = find_cheapest_price(n, flights, start, destination, k)
print(result)
