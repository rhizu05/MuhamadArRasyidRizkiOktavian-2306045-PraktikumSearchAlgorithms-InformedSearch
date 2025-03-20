from queue import PriorityQueue

# Fungsi untuk algoritma A* Graph Search
def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan f(n) = g(n) + h(n)
    frontier.put((0, start, []))  # (total_cost, node, path)
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        current_cost, current_node, path = frontier.get()  # Ambil simpul dengan prioritas terendah
        
        if current_node in explored:
            continue

        path = path + [current_node]
        explored.add(current_node)  # Tandai simpul sebagai telah dieksplorasi

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", current_cost)
            return path, current_cost

        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                total_cost = current_cost + cost + heuristic[neighbor]  # g(n) + h(n)
                frontier.put((total_cost, neighbor, path))  # Masukkan simpul ke frontier

    print("\nSimpul tujuan tidak ditemukan!")
    return None, float("inf")  # Jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'G': 0,
}

# Graf berbentuk adjacency list dengan bobot
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'B': 1, 'D': 5},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1},
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi A* Graph Search
a_star_graph_search(graph, start_node, goal_node, heuristic)