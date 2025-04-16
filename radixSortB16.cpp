#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> a, b;
vector<int> fr(1 << 16);

void radixSort16(vector<int>& a, int n, int mx) {

    for(int i = 1; i <= n; i++)
        a[i] += mx;

    for (int i = 0; i < 32; i += 16) {
        for (int j = 1; j <= n; j++) {
            fr[(a[j] >> i) & 0xFFFF]++;
        }
        for (int j = 1; j <= (1 << 16); j++) {
            fr[j] += fr[j - 1];
        }
        for (int j = n; j >= 1; j--) {
            b[fr[(a[j] >> i) & 0xFFFF]--] = a[j];
        }
        for (int j = 1; j <= n; j++) {
            a[j] = b[j];
        }
        fill(fr.begin(), fr.end(), 0);
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
        radixSort16(a, n, mx);
        for (int i = 1; i <= n; i++) fout << a[i] << " ";
        fout << '\n';
        a.clear();
        b.clear();
    }
    return 0;
}
