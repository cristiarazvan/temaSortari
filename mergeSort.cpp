#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> a;
vector<int> tmp;

void mergeSort(vector<int>& a, int st, int dr) {
    if (st + 1 < dr) {
        int mid = (st + dr) >> 1;
        mergeSort(a, st, mid);
        mergeSort(a, mid + 1, dr);
        int l, r, p;
        l = st;
        r = mid + 1;
        p = 0;
        while (l <= mid && r <= dr)
            if (a[l] < a[r])
                tmp[p++] = a[l++];
            else
                tmp[p++] = a[r++];
        while (l <= mid) tmp.push_back(a[l++]);
        while (r <= dr) tmp.push_back(a[r++]);
        for (int i = st, p = 0; i <= dr; i++, p++) a[i] = tmp[p];
    }
}

int main() {
    fin >> t;
    while (t--) {
        fin >> n >> mx;
        for (int i = 0; i < n; i++) fin >> a[i];
        mergeSort(a, 0, n - 1);
        for (int i : a) fout << i << " ";
        fout << '\n';
    }

    return 0;
}
