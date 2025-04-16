#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> a, b;
vector<int> fr(10);

void radixSort10(vector<int>& a, int n, int mx) {
    for(int i = 1; i <= n; i++)
        a[i] += mx;
    int exp = 1;
    while ((mx << 1) / exp > 0) {
        for (int i = 1; i <= n; i++) fr[(a[i] / exp) % 10]++;
        for (int i = 1; i < 10; i++) fr[i] += fr[i - 1];
        for (int i = n; i >= 1; i--) b[fr[(a[i] / exp) % 10]--] = a[i];
        for (int i = 1; i <= n; i++) a[i] = b[i];
        fill(fr.begin(), fr.end(), 0);
        exp *= 10;
    }
    for(int i = 1; i <= n; i++)
        a[i] -= mx;
}
int main() {
    fin >> t;
    while (t--) {
        fin >> n >> mx;
        a.resize(n + 1);
        b.resize(n + 1);
        for (int i = 1; i <= n; i++) fin >> a[i];
        radixSort10(a, n, mx);
        for (int i = 1; i <= n; i++) fout << a[i] << " ";
        fout << '\n';
        a.clear();
        b.clear();
    }
    return 0;
}
