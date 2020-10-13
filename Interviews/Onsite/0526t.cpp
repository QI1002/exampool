
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

class Dictionary {
private:
  vector<string> strs;
public:
  Dictionary(initializer_list<string> list) {
    strs = list;
  }

  string getWord(int index) const {
    if (index >= strs.size()) return "";
    return strs[index];
  }
};

class UpsideMap {
 protected:
  unordered_map<char, char> m;
  typedef pair<char, char> pairchar;
  virtual vector<pairchar> getMap() = 0;
 public:
  void generate() {
    vector<pairchar> h = getMap();
    for(auto p: h) {
      assert(!m.count(p.first));
      m[p.first] = p.second;
      if (p.first == p.second) continue;
      assert(!m.count(p.second));
      m[p.second] = p.first;
    }
  }
};

class UpsideMapLC : public UpsideMap {
 private:
  vector<pairchar> h = {
    {'a', 'e'}, {'b', 'q'}, {'d', 'p'}, {'f', 't'}, {'h', 'y'}, {'i', 'i'},
    {'l', 'l'}, {'m', 'w'}, {'n', 'u'}, {'o', 'o'}, {'s', 's'}, {'x', 'x'}, {'z','z'}};
 protected:
  virtual vector<pairchar> getMap() { return h; }
};

class UpsideMapDigit : public UpsideMap {
 private:
  vector<pairchar> h =
   {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}};
 protected:
  virtual vector<pairchar> getMap() { return h; }
};

template<typename T> class Upside : public T {
private:
  using T::generate;
  using T::m;
public:
  Upside() { generate(); }
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
    int n = s.length(), nn = (n+1)/2;
    for (int i = 0; i < nn; ++i) {
        int c = s[i];
        if (m[c] != s[n-i-1]) return false;
    }
    return true;
  }
};

typedef Upside<UpsideMapLC>    UpsideLC;
typedef Upside<UpsideMapDigit> UpsideDigit;

template<typename T> class Upside2 : public T {
private:
  using T::generate;
  using T::m;
public:
  Upside2() { generate(); }
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
      int n = s.length(), nn = (n+1)/2;
      bool f = false;
      for (int i = 0; i < nn; ++i) {
          int c = s[i];
          int d = s[n-i-1];
          if (m[c] == 0 || m[d] == 0) return false;
          if (m[c] != d) f = true;
      }
      return f;
  }
};

typedef Upside2<UpsideMapLC>    UpsideLC2;
typedef Upside2<UpsideMapDigit> UpsideDigit2;

int main(int argc, char **argv) {
  UpsideLC  uslc;
  UpsideLC2 uslc2;
  Dictionary dictLC = { "axe", "dip", "dollop", "mow", "hello", "omw" };
  vector<string> result1 = uslc.allUpSide(dictLC);
  for(auto s: result1) cout << s << " "; cout << endl;
  vector<string> result2 = uslc2.allUpSideDiff(dictLC);
  for(auto s: result2) cout << s << " "; cout << endl;

  UpsideDigit  usgt;
  UpsideDigit2 usgt2;
  Dictionary dictDigit = { "123", "121", "696", "689", "081", "152", "101", "6699", "969", "1221", "888" };
  vector<string> result3 = usgt.allUpSide(dictDigit);
  for(auto s: result3) cout << s << " "; cout << endl;
  vector<string> result4 = usgt2.allUpSideDiff(dictDigit);
  for(auto s: result4) cout << s << " "; cout << endl;

  return 0;
}

