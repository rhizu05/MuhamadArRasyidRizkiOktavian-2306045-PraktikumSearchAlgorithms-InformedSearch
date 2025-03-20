from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Best-First Search
def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan heuristik
    frontier.put((heuristic[start], start))  # Menambahkan simpul awal dengan nilai heuristik
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi
    visited_order = []  # List untuk mencatat urutan kunjungan simpul
    heuristic_usage_count = 0  # Penghitung jumlah akses heuristik

    while not frontier.empty():
        _, current_node = frontier.get()  # Ambil simpul dengan heuristik terendah
        visited_order.append(current_node)
        print("Mengunjungi simpul:", current_node)

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:", " → ".join(visited_order))
            print("Jumlah akses heuristik:", heuristic_usage_count)
            return True  # Berhenti jika simpul tujuan ditemukan

        explored.add(current_node)  # Tandai sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Nilai heuristik sebagai prioritas
                heuristic_usage_count += 1  # Tambah jumlah akses heuristik
                frontier.put((priority, neighbor))  # Tambahkan ke antrian

    print("\nSimpul tujuan tidak ditemukan!")
    print("Urutan kunjungan simpul:", " → ".join(visited_order))
    print("Jumlah akses heuristik:", heuristic_usage_count)
    return False  # Jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'G': 0,
}

# Graf berbentuk adjacency list
graph = {
    'S': {'A', 'B'},
    'A': {'B', 'D'},
    'B': {'C', 'D'},
    'C': {'D', 'G'},
    'D': {'G'},
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi Greedy Best-First Search
greedy_best_first_search(graph, start_node, goal_node)
