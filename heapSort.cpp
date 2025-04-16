#include <fstream>
#include <utility>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> a;

void heapDown(vector<int> &a, int d, int i) {
    int best = i;
    int l = (i << 1);
    int r = (i << 1) | 1;
    if (l <= d && a[l] > a[best]) best = l;
    if (r <= d && a[r] > a[best]) best = r;
    if (best != i) {
        swap(a[i], a[best]);
        heapDown(a, d, best);
    }
}

void heapSort(vector<int> &a, int n) {
    for (int i = n / 2; i >= 1; i--) heapDown(a, n, i);
    for (int i = n; i > 1; i--) {
        swap(a[1], a[i]);
        heapDown(a, i - 1, 1);
    }
}

int main() {
    fin >> t;

    while (t--) {
        fin >> n >> mx;
        a.resize(n + 1);
        for (int i = 1; i <= n; i++) fin >> a[i];
        heapSort(a, n);
        for (int i = 1; i <= n; i++) fout << a[i] << " ";
        fout << "\n";
        a.clear();
    }

    return 0;
}
