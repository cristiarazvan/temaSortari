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

int partition5Med(vector<int> &arr, int start, int end){
    if ( end - start < 5 ){
        return partitionEnd(arr, start, end);
    }
    int mid  = (start+end)/2 + 1;
    vector<int> list;
    list.push_back(arr[start]);
    list.push_back(arr[(start+mid)/2]);
    list.push_back(arr[mid]);
    list.push_back(arr[(end+mid)/2]);
    list.push_back(arr[end]);

    for (int i = 1; i < (int)list.size(); i++){
        int key = list[i];
        int j = i - 1;
        while(j >= 0 && list[j] > key){
            list[j+1] = list[j];
            j--;
        }
        list[j+1] = key;
    }

    int median = list[2]; 

    int pivot = start;
    for ( int i = start ; i <= end; i++ ){
        if ( arr[i] == median ){
            pivot = i; 
            break;
        }
    }

    if ( pivot != end ){
        swap(arr[pivot], arr[end]);
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
    if (start >= end) return; 
    int pivot = partition5Med(arr, start, end);
    quick_sort(arr, start, pivot-1);
    quick_sort(arr, pivot+1, end);
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