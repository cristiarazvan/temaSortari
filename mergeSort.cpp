#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> a;
vector<int> tmp;

void mergeSort(vector<int>& a, int st, int dr) {
    if (st < dr) {
        int mid = (st + dr) / 2;
        mergeSort(a, st, mid);
        mergeSort(a, mid + 1, dr);
        
        
        int l = st;
        int r = mid + 1;
        int p = 0;
        
        while (l <= mid && r <= dr) {
            if (a[l] < a[r])
                tmp[p++] = a[l++];
            else
                tmp[p++] = a[r++];
        }
        
        while (l <= mid)
            tmp[p++] = a[l++];
            
        while (r <= dr)
            tmp[p++] = a[r++];
            
        for (int i = 0; i < p; i++)
            a[st + i] = tmp[i];
    }
}

int main() {
    fin >> t;
    while (t--) {
        fin >> n >> mx;
        a.resize(n);
        tmp.resize(n);
        for (int i = 0; i < n; i++) fin >> a[i];
        
       
        
        mergeSort(a, 0, n - 1);
        
        for (int i = 0; i < n; i++) fout << a[i] << " ";
        fout << '\n';
    }

    return 0;
}
