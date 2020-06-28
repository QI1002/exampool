  
#include <algorithm>
#include <iostream>
#include <utility>

#include <cstring>
#include <climits>
#include <ostream>
#include <sstream>
#include <string>
#include <vector>
#include <memory>
#include <functional>
#include <unordered_set>
#include <unordered_map>

using namespace std;
void qsort(vector<int>& h, int i, int j) {   
    int a, b, c;
    if (i >= j) return;
    a = i-1; b = j, c = h[j];
    while(true) {
      for(++a; h[++a] < h[j]; ++a);
      for(--b; b >= 0 && h[b] > h[j]; --b);
      if (a >= b) break;
      swap<int>(h[a], h[b]);
    }

    swap<int>(h[a], h[j]);
    qsort(h, i, a-1);
    qsort(h, a+1, j);
}

void sort(vector<int>& h) {
    qsort(h, 0, h.size()-1);
}

void sort2(vector<int> &s, int l = INT_MIN, int r = INT_MIN)
{
    if (l == INT_MIN) l = 0;
    if (r == INT_MIN) r = s.size()-1;
    if (l >= r) return;

    int i = l-1;
    int j = r;
    int a = s[r];

    while(true)
    {
        while(s[++i] < a);
        while(i < j && s[--j] > a);    
        if (i >= j) break;
        swap<int>(s[i], s[j]);
    }

    //swap<int>(s[i], s[r]);
    swap<int>(s[j], s[r]);
    sort2(s, l, i-1);
    sort2(s, i+1, r);
}

int main(void) 
{
#if 0
  //vector<int> h = {2,3,1,5,4};
  //vector<int> h = {3, 15, 17, 29, 15, 5, 0, 6, 1, 27, 3, 22, 21, 9, 8, 16, 25, 6, 27, 3};
  //vector<int> h = {2, 26, 10, 0, 15, 22, 27, 9, 2, 1, 28, 8, 25, 10, 4, 1, 8, 27, 16, 9, 2, 5, 6, 21};
  vector<int> h = {3, 3, 23, 21, 26, 21, 13};
#else
  vector<int> h;
  srand(time(NULL));
  int n = rand() % 20 + 5;
  for (int i = 0; i < n; i++) h.emplace_back(rand() % 30);
#endif
  for(auto t: h) cout << t << " "; cout << endl;
  sort2(h);
  for(auto t: h) cout << t << " "; cout << endl;
  return 0; 
} 

