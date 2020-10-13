
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
  static const char invalid = 0;
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
  int getUpside(int c) {
    if (m.size() == 0) generate();
    auto it = m.find(c);
    if (it == m.end()) return invalid;
    return it->second;
  }
  static bool valid(int v) { return v != invalid; }
};
const char UpsideMap::invalid;

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

class Upside {
public:
  Upside() { }

  vector<string> allUpSide(const Dictionary& dict, UpsideMap *map) {
    vector<string> r;
    for(int i = 0; ; ++i) {
        string s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSide(s, map)) r.emplace_back(s);
    }
    return r;
  }

  bool isUpSide(const string &s, UpsideMap* map) {
    int n = s.length(), nn = (n+1)/2;
    for (int i = 0; i < nn; ++i) {
        int c = s[i];
        int d = map->getUpside(c);
        if (!map->valid(d)) return false;
        if (d != s[n-i-1]) return false;
    }
    return true;
  }
};

class Upside2 {
public:
  Upside2() { }
  vector<string> allUpSideDiff(const Dictionary& dict, UpsideMap *map) {
    vector<string> r;
    for(int i = 0; ; ++i) {
        string s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSideDiff(s, map)) r.emplace_back(s);
    }
    return r;
  }
  bool isUpSideDiff(const string &s, UpsideMap *map) {
      int n = s.length(), nn = (n+1)/2;
      bool f = false;
      for (int i = 0; i < nn; ++i) {
          int c = s[i];
          int d = s[n-i-1];
          int cc = map->getUpside(c);
          int dd = map->getUpside(d);
          if (!map->valid(cc) || !map->valid(dd)) return false;
          if (cc != d) f = true;
      }
      return f;
  }
};

int main(int argc, char **argv) {
  Upside us;
  Upside2 us2;

  Dictionary dictLC = { "axe", "dip", "dollop", "mow", "hello", "omw" };
  UpsideMapLC mapLC;
  vector<string> result1 = us.allUpSide(dictLC, &mapLC);
  for(auto s: result1) cout << s << " "; cout << endl;
  vector<string> result2 = us2.allUpSideDiff(dictLC, &mapLC);
  for(auto s: result2) cout << s << " "; cout << endl;

  Dictionary dictDigit = { "123", "121", "696", "689", "081", "152", "101", "6699", "969", "1221", "888" };
  UpsideMapDigit mapDigit;
  vector<string> result3 = us.allUpSide(dictDigit, &mapDigit);
  for(auto s: result3) cout << s << " "; cout << endl;
  vector<string> result4 = us2.allUpSideDiff(dictDigit, &mapDigit);
  for(auto s: result4) cout << s << " "; cout << endl;
  return 0;
}

