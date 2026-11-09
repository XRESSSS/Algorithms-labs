#include <iostream>
#include <cstring>

using namespace std;

#define INF 9999999

#define V 8

int G[V][V] = {
    // 1    2    3    4    5    6    7    8
    {INF,   8,   2,   4,   3, INF, INF, INF}, // 1
    {  8, INF, INF, INF,   6,   3, INF, INF}, // 2
    {  2, INF, INF,   6, INF,   7, INF,   4}, // 3
    {  4, INF,   6, INF,   1, INF, INF, INF}, // 4
    {  3,   6, INF,   1, INF, INF,   4, INF}, // 5
    {INF,   3,   7, INF, INF, INF,   3,   1}, // 6
    {INF, INF, INF, INF,   4,   3, INF,   5}, // 7
    {INF, INF,   4, INF, INF,   1,   5, INF}  // 8
};

int main() {
    int no_edge = 0; // лічильник ребер у МКД
    bool selected[V];

    // Спочатку всі вершини не вибрані
    memset(selected, false, sizeof(selected));

    // Обираємо першу вершину (індекс 0 відповідає вершині 1)
    selected[0] = true;

    int x; // індекс рядка (вершина з V_T)
    int y; // індекс стовпця (вершина з V - V_T)
    int total_weight = 0;

    cout << "Edge" << " : " << "Weight" << endl;

    // Кількість ребер у МКД завжди дорівнює V - 1
    while (no_edge < V - 1) {
        int min = INF;
        x = 0;
        y = 0;

        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    if (!selected[j] && G[i][j] != INF) {
                        if (min > G[i][j]) {
                            min = G[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }

        cout << (x + 1) << " - " << (y + 1) << " : " << G[x][y] << endl;
        total_weight += G[x][y];
        selected[y] = true;
        no_edge++;
    }

    cout << "Total MST Weight: " << total_weight << endl;

    return 0;
}
