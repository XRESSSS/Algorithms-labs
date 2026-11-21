import sys
V = 8               # Кількість вершин графа
INF = float('inf')  # Нескінченність
# Матриця ваг графа (індексація з 1 до V)
graph = [[0] * (V + 1) for _ in range(V + 1)]
# Допоміжна функція для додавання неорієнтованого ребра
def add_edge(u: int, v: int, weight: int) -> None:
    graph[u][v] = weight
    graph[v][u] = weight
def extract_min_from_pq(dist: list[float], in_pq: list[bool]) -> int:
    min_val = INF
    min_vertex = -1
    for v in range(1, V + 1):
        if in_pq[v] and dist[v] < min_val:
            min_val = dist[v]
            min_vertex = v
    if min_vertex != -1:
        in_pq[min_vertex] = False
    return min_vertex
# Рекурсивне формування шляху від стартової вершини до v
def get_path(pred: list[int], v: int) -> str:
    if pred[v] == -1:
        return str(v)
    return get_path(pred, pred[v]) + f" -> {v}"
def dijkstra(s: int) -> None:
    pred = [-1] * (V + 1)
    dist = [INF] * (V + 1)
    in_pq = [False] * (V + 1)
    pq_size = 0
    # Ініціалізація
    for v in range(1, V + 1):
        pred[v] = -1
        if v != s:
            dist[v] = INF
        else:
            dist[v] = 0
        in_pq[v] = True  # InsertInPQ(pq, v, dist[v])
        pq_size += 1
    # Основний цикл
    while pq_size != 0:
        u = extract_min_from_pq(dist, in_pq)
        if u == -1:
            break
        pq_size -= 1
        for v in range(1, V + 1):
            if graph[u][v] != 0 and in_pq[v]:
                # Умова релаксації (рядок 14)
                if dist[u] != INF and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    pred[v] = u
                    # UpdatePQ виконується автоматично через оновлення dist[v]
    # Вивід результатів
    print("Path : Weight")
    for v in range(1, V + 1):
        if v == s:
            continue
        print(f"{get_path(pred, v)} : {int(dist[v])}")
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    # Ребра графа (Варіант 17)
    add_edge(1, 2, 3)
    add_edge(1, 3, 2)
    add_edge(1, 4, 4)
    add_edge(1, 6, 8)
    add_edge(2, 5, 6)
    add_edge(2, 6, 3)
    add_edge(3, 4, 6)
    add_edge(3, 6, 7)
    add_edge(3, 8, 4)
    add_edge(4, 5, 1)
    add_edge(5, 7, 4)
    add_edge(6, 7, 3)
    add_edge(6, 8, 1)
    add_edge(7, 8, 5)
    start_node = 1
    dijkstra(start_node)
