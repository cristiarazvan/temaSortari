#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


ifstream fin("teste.in");
ofstream fout("teste.out");



const int MIN_RUN = 32;

int t, n, mx;
vector<int> arr;

void insertionSort(vector<int>& arr, int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int current = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > current) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = current;
    }
}

void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> leftPart(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> rightPart(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;

    while (i < leftPart.size() && j < rightPart.size()) {
        if (leftPart[i] <= rightPart[j]) {
            arr[k++] = leftPart[i++];
        } else {
            arr[k++] = rightPart[j++];
        }
    }

    while (i < leftPart.size()) {
        arr[k++] = leftPart[i++];
    }

    while (j < rightPart.size()) {
        arr[k++] = rightPart[j++];
    }
}

void timSort(vector<int>& arr) {
    int n = arr.size();

    for (int start = 0; start < n; start += MIN_RUN) {
        int end = min(start + MIN_RUN - 1, n - 1);
        insertionSort(arr, start, end);
    }

    for (int size = MIN_RUN; size < n; size *= 2) {
        for (int left = 0; left < n; left += 2 * size) {
            int mid = min(left + size - 1, n - 1);
            int right = min(left + 2 * size - 1, n - 1);

            if (mid < right) {
                merge(arr, left, mid, right);
            }
        }
    }
}


int main() {

    fin >> t;
    while(t--){
        fin >> n >> mx;
        arr.resize(n);
        for(int i = 0; i < n; i++)
            fin >> arr[i];
        timSort(arr);
        for(int i = 0; i < n; i++)
            fout << arr[i] << " ";
        fout << '\n';
        arr.clear();
    }    

    return 0;
}