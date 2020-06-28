//g++ -std=gnu++11 leetcode.cpp
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
#include <unordered_set>
#include <math.h>
#include <set>
#include <list>
#include <random>
#include <time.h>

using namespace std;

class MySort{
private:
    void qsort(vector<int>& v, int left, int right) {
        if (left >= right) return; 
        int i = left, j = right-1;
        int m = v[right];
        while (true) {
            for(; v[i] < m; i++); // < : anchor in the end
            for(; j >= 0 && v[j] >= m; j--); // invert with previous
            if (i >= j) break; // >= not > due to = is no use in the next  
            swap<int>(v[i], v[j]);     
        }
        swap<int>(v[right], v[i]);
        qsort(v, left, i-1);
        qsort(v, i+1, right); 
    }
public:
    void sort(vector<int> &v) {
        qsort(v, 0, v.size()-1);
    }
};

int main(int argc, char* argv[]) {
    MySort s;
    srand(time(NULL));
    for(int i = 0; i < 10; i++) {
        int n = random() % 20 + 1;
        vector<int> v;
        for(int j = 0; j < n; j++) v.emplace_back(random() % 100);
        s.sort(v);
        for(auto g: v) cout << g << " "; cout << endl;
    }
    return 0;
}

