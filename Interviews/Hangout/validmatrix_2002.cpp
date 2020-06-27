//g++ -std=gnu++11 templ.cpp
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
#include <unordered_set>
#include <unordered_map>
#include <math.h>
#include <set>
#include <map>
#include <list>
#include <random>
#include <time.h>
#include <deque>
#include <queue>
#include <climits>

using namespace std;

int valid(vector<int> &a) {
  int j = 0, k = 0;
  for(auto t:a) {
      if (t == 0) ++j;
      else {
	  k += j*(j+1)/2;
	  j = 0;
      } 
  }
  if (j) k+= j*(j+1)/2;
  return k;
}

int valid2D(vector<vector<int>>& A) {
    int rowc = A.size(); if (rowc == 0) return 0;
    int colc = A[0].size(); if (colc == 0) return 0;
    int i, j, k, r = 0;
    for(i = 0; i < rowc; ++i) {
	vector<int>& v = A[i];
	r += valid(v);
	for(j = i+1; j < rowc; ++j) {
            for(k = 0; k <= colc; ++k) v[k] |= A[j][k];
            r += valid(v); 	    
	}
    } 
   return r;
}

int main(int argc, char* argv[]) {
    srand(time(NULL));
    //vector<int> A = {0,0,1,0,0,0};
    vector<int> A = {0,0,1,0,0,0,1};
    cout << valid(A) << endl;
    vector<vector<int>> B = {{1,0,0},{0,1,0},{1,1,1}};
    cout << valid2D(B) << endl;
    return 0;
}

