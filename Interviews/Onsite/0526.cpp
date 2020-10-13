  
#include <algorithm>
#include <iostream>
#include <utility>

#include <cassert>
#include <cstring>
#include <climits>
#include <ostream>
#include <sstream>
#include <list>
#include <string>
#include <deque>
#include <vector>
#include <memory>
#include <functional>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pairint;
class Dictionary {
private:
  vector<string> strs;
public:
  //Dictionary() { }
  //Dictionary(const vector<string> data) {
  //  strs = data;
  //}
  Dictionary(initializer_list<string> list) {
    strs = list;
  }

  string getWord(int index) const { 
    if (index >= strs.size()) return "";
    return strs[index];
  }
};

class Upside {
private:
  vector<pairint> h = {
    {'a', 'e'}, {'b', 'q'}, {'d', 'p'}, {'f', 't'}, {'h', 'y'}, {'i', 'i'},
    {'l', 'l'}, {'m', 'w'}, {'n', 'u'}, {'o', 'o'}, {'s', 's'}, {'x', 'x'}, {'z','z'}};
protected:
  unordered_map<int, int> m;

public:
  Upside() {
    for(auto p: h) {
      assert(!m.count(p.first));
      m[p.first] = p.second;
      if (p.first == p.second) continue;
      assert(!m.count(p.second));
      m[p.second] = p.first;
    }
  }

  vector<string> allUpSide(const Dictionary& dict) {
    vector<string> r;
    for(int i = 0; ; ++i) {
        string s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSide(s)) r.emplace_back(s);
    }
    return r;
  }

  bool isUpSide(const string &s) {
    int n = s.length(), nn = n/2;
    for (int i = 0; i < nn; ++i) {
        int c = s[i];
        if (m[c] != (int)s[n-i-1]) return false;     
    } 
    if (n & 1) { // odd length
       int c = s[nn];
       if (c != m[c]) return false; 
    }
    return true;
  }  
};

class Upside2 : public Upside {
public:
  Upside2() : Upside() { }
  vector<string> allUpSideDiff(const Dictionary& dict) {
    vector<string> r;
    for(int i = 0; ; ++i) {
        string s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSideDiff(s)) r.emplace_back(s);
    }
    return r;
  }
  bool isUpSideDiff(const string &s) {
      int n = s.length(), nn = n/2;
      bool f = false;
      for (int i = 0; i < nn; ++i) {
          int c = s[i];
          int d = s[n-i-1];
          if (m[c] == 0 || m[d] == 0) return false;
          if (m[c] != d) f = true;
      } 
      if (n & 1) { // odd length
         int c = s[nn];
         if (m[c] == 0) return false;
         if (c != m[c]) f = true;
      }
      return f;
  }
};

int main(int argc, char **argv) {
  Dictionary dict = { "axe", "dip", "dollop", "mow", "hello", "omw" };
  Upside us; 
  vector<string> result = us.allUpSide(dict);
  for(auto s: result) cout << s << " "; cout << endl;

  Upside2 us2; 
  vector<string> result2 = us2.allUpSideDiff(dict);
  for(auto s: result2) cout << s << " "; cout << endl;
  return 0;
}

