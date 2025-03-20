from queue import PriorityQueue

# Fungsi untuk algoritma A* Tree Search
def a_star_tree_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan f(n) = g(n) + h(n)
    frontier.put((heuristic[start], 0, start, []))  # (f(n), g(n), node, path)
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi

    while not frontier.empty():
        _, g_cost, current_node, path = frontier.get()  # Ambil simpul dengan prioritas terendah

        # Jika sudah dieksplorasi, lewati
        if current_node in explored:
            continue

        path = path + [current_node]
        explored.add(current_node)  # Tandai simpul sebagai telah dieksplorasi

        # Jika mencapai tujuan
        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", g_cost)
            return path, g_cost

        # Eksplorasi tetangga
        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                new_g_cost = g_cost + cost  # Perbarui g(n)
                f_cost = new_g_cost + heuristic[neighbor]  # Hitung f(n) = g(n) + h(n)
                frontier.put((f_cost, new_g_cost, neighbor, path))  # Tambahkan ke antrian

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

# Panggil fungsi A* Tree Search
a_star_tree_search(graph, start_node, goal_node, heuristic)
