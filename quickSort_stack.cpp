#include <fstream>
#include <vector>
#include <stack>

std::ifstream fin("teste.in");
std::ofstream fout("teste.out");

int t, n, mx;
std::vector<int> arr;

void insertionSort(std::vector<int>& arr, int start, int low) {
    for (int i = start + 1; i <= low; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= start && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int medianOfThree(std::vector<int>& arr, int start, int end) {
    int mid = start + (end - start) / 2;
    
    if (arr[start] > arr[mid]) std::swap(arr[start], arr[mid]);
    if (arr[start] > arr[end]) std::swap(arr[start], arr[end]);
    if (arr[mid] > arr[end]) std::swap(arr[mid], arr[end]);

    std::swap(arr[mid], arr[end]);
    return arr[end];
}

int partition3Med(std::vector<int>& arr, int start, int end){
    int pivot = medianOfThree(arr, start, end);
    int i = start - 1;

    for ( int j = start; j < end; j++){
        if ( arr[j] <= pivot ){
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i+1], arr[end]);
    return i+1;
}

void quick_sort(std::vector<int>& arr, int start, int end){
    std::stack<int> s;
    s.push(start);
    s.push(end);

    while ( !s.empty()){
        start = s.top();
        s.pop();
        end = s.top();
        s.pop();

        int pivot = partition3Med(arr, start, end);

        if ( pivot - 1 > start ){
            s.push(start);
            s.push(pivot - 1);
        }

        if ( pivot + 1 < end){
            s.push(pivot + 1);
            s.push(end);
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
        quick_sort(arr, 0 , n-1);
        for(int i = 0; i < n; i++)
            fout << arr[i] << " ";
        fout << '\n';
        arr.clear();
    }

    return 0;
}