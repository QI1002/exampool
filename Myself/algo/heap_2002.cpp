  
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

void upheap(vector<int> &h, int g) {
    int j, i = h.size();
    h.emplace_back(g);
    while(i != 1) {
       j = i/2;
       if (h[j] > h[i]) swap<int>(h[j], h[i]);
       else break;
       i = j;
    }     
}

int downheap(vector<int> &h) {
    int r = h[1];
    h[1] = h.back(); h.pop_back();
    int n = h.size(), j, i = 1;
    while(true) {
        j = 2*i+1; 
        if (j < n) {
            if (h[j] > h[j-1]) --j;
        }else if (--j >= n) break;
        if (h[j] >= h[i]) break;
        swap<int>(h[j], h[i]); i = j;         
    }
    return r;
}

void sort(vector<int> &h) {
  vector<int> t(1);
  for(auto g: h) upheap(t, g);
  for(int i = 0; i < h.size(); i++) h[i] = downheap(t);
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
  sort(h);
  for(auto t: h) cout << t << " "; cout << endl;
  return 0; 
} 

