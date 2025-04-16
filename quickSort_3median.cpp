#include <fstream>
#include <vector>

using namespace std;

ifstream fin("teste.in");
ofstream fout("teste.out");

int t, n, mx;
vector<int> arr;

int partition3Med(vector<int> &arr, int start, int end){
    int key = start;
    int mid = (start+end)/2 + 1;
    if (( arr[start] <= arr[mid] && arr[mid] < arr[end] ) || ( arr[end] <= arr[mid] && arr[mid] <= arr[start])){
        key = mid;
    } else if(( arr[mid] <= arr[end] && arr[end] <= arr[start] ) || ( arr[start] <= arr[end] && arr[end] <= arr[mid])){
        key = end;
    }

    if ( key != end ){
        swap(arr[key], arr[end]);
    }

    int i = start;

    for ( int j = start; j < end; j++ ){
        if ( arr[j] < arr[end] ){
            swap(arr[i], arr[j]);
            i++;
        }
    }

    swap(arr[end], arr[i]);

    return i;
}

void quick_sort(vector<int> &arr, int start, int end){
    if ( start < end ){
        int pivot = partition3Med(arr, start, end);
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