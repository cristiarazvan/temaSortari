#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");


int t, n, mx;
vector<int> arr;

void shell_sort(vector<int> &arr){
    int n = arr.size();
    for ( int g = n/2; g >= 1; g /= 2){
        for ( int i = g; i < n; i++){
            int temp = arr[i];
            int j = i;

            while ( j >= g && arr[j-g] > temp){
                arr[j] = arr[j-g];
                j -= g;
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
        for(int i = 0; i < n; i++)
            fin >> arr[i];
        shell_sort(arr);
        for(int i = 0; i < n; i++)
            fout << arr[i] << " ";
        fout << '\n';
        arr.clear();
    }

    return 0;
}