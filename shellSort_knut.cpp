#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> arr;

void shell_sort_knutt(vector<int> &arr){
    int n = arr.size();

    int gap = 1;
    while ( gap < n/3 ){
        gap *= 3;
        gap++;
    }

    for (; gap >= 1; gap /= 3 ){
        for ( int i = 1; i < n; i++){
            int temp = arr[i];
            int j = i;
            while ( j >= gap && arr[j-gap] > temp){
                arr[j] = arr[j-gap];
                j -= gap;
            }

            arr[j] = temp;
        }
    }
}

int main(){
    fin >> t;
    while(t--){
        fin >> n >> mx;
        arr.resize(n);
        for ( int i = 0; i < n; i++){
            fin >> arr[i];
        }
        shell_sort_knutt(arr);
        for ( int i = 0; i < n; i++){
            fout << arr[i] << " ";
        }
        fout << '\n';
        arr.clear();
    }

    return 0;
}