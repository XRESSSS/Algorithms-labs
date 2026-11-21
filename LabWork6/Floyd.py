import sys

N = 8          # Кількість вершин графа
INF = 99999    # Умовна нескінченність


# Допоміжна функція для додавання неорієнтованого ребра
def add_edge(W: list[list[int]], u: int, v: int, weight: int) -> None:
    W[u][v] = weight
    W[v][u] = weight


def floyd(W: list[list[int]]) -> list[list[int]]:
    # D <- W
    D = [row[:] for row in W]

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]

    return D


def print_matrix(D: list[list[int]]) -> None:
    header = "    " + "".join(f"{j:4d}" for j in range(1, N + 1))
    print(header)
    for i in range(1, N + 1):
        row_str = f"{i:2d}: "
        for j in range(1, N + 1):
            if D[i][j] == INF:
                row_str += " INF"
            else:
                row_str += f"{D[i][j]:4d}"
        print(row_str)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")

    # Ініціалізація початкової вагової матриці W
    W = [[0 if i == j else INF for j in range(N + 1)] for i in range(N + 1)]

    # Ребра графа 
    add_edge(W, 1, 2, 3)
    add_edge(W, 1, 3, 2)
    add_edge(W, 1, 4, 4)
    add_edge(W, 1, 6, 8)
    add_edge(W, 2, 5, 6)
    add_edge(W, 2, 6, 3)
    add_edge(W, 3, 4, 6)
    add_edge(W, 3, 6, 7)
    add_edge(W, 3, 8, 4)
    add_edge(W, 4, 5, 1)
    add_edge(W, 5, 7, 4)
    add_edge(W, 6, 7, 3)
    add_edge(W, 6, 8, 1)
    add_edge(W, 7, 8, 5)

    D = floyd(W)

    print("Матриця найкоротших відстаней D (алгоритм Флойда):")
    print_matrix(D)
