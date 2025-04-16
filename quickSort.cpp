#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> arr;

int partitionEnd(vector<int> &arr, int start, int end){
    int i = start;

    for (int j = start; j < end; j++){
        if (arr[j] < arr[end]){
            swap(arr[i], arr[j]);
            i++;
        }
    }

    swap(arr[end], arr[i]);

    return i;
}


void quick_sort(vector<int> &arr, int start, int end){
    if ( start < end ){
        int pivot = partitionEnd(arr, start, end);
        quick_sort(arr, start, pivot-1);
        quick_sort(arr, pivot+1, end);
    }
}

int main(){
    fin >> t;
    while(t--){
        fin >> n >> mx;
        arr.resize(n);
        for(int i = 0; i < n; i++)
            fin >> arr[i];
        quick_sort(arr, 0, n-1);
        for(int i = 0; i < n; i++)
            fout << arr[i] << " ";
        fout << '\n';
        arr.clear();
    }

    return 0;
}