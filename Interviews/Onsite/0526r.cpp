
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

class UpsideType;
typedef reference_wrapper<UpsideType> UpsideRef;

class UpsideType {
 protected:
  typedef pair<char, char> pairchar;
  static const char invalid = ' ';
  unordered_map<char, char> m; char c_;
 public:
  UpsideType() { c_ = invalid; }
  virtual UpsideType& getUpside() = 0;
  virtual bool equal(UpsideType& f) = 0;
  bool operator==(UpsideType& f) { return equal(f); }
  bool operator!=(UpsideType& f) { return !equal(f); }
  bool valid() { return c_ != invalid; }
  void print() { cout << c_; }
};
const char UpsideType::invalid;


class UpsideLC : public UpsideType {
 private:
  static const vector<pairchar> h;
  UpsideLC* p;
 public:
  UpsideLC(const char &c) {
    p = NULL;
    if ('a' <= c && c <= 'z') c_ = c;
  }
  void initMap() {
    for(auto p: h) {
      assert(!m.count(p.first));
      m[p.first] = p.second;
      if (p.first == p.second) continue;
      assert(!m.count(p.second));
      m[p.second] = p.first;
    }
  }
  UpsideType& getUpside() {
    if (!m.size()) initMap();
    if (p) delete p;
    p = new UpsideLC(m.count(c_) ? m[c_] : invalid);
    return *p;
  }
  bool equal(UpsideType& f) {
    if (typeid(f) != typeid(*this)) return false;
    UpsideLC& ff = static_cast<UpsideLC&>(f);
    if (!valid() || !ff.valid()) return false;
    return c_ == ff.c_;
  }
};
const vector<UpsideLC::pairchar> UpsideLC::h =
   {{'a', 'e'}, {'b', 'q'}, {'d', 'p'}, {'f', 't'}, {'h', 'y'}, {'i', 'i'},
    {'l', 'l'}, {'m', 'w'}, {'n', 'u'}, {'o', 'o'}, {'s', 's'}, {'x', 'x'}, {'z','z'}};

class UpsideDigit : public UpsideType {
 private:
  static const vector<pairchar> h;
  UpsideDigit* p;
 public:
  UpsideDigit(const char &c) {
    p = NULL;
    if ('0' <= c && c <= '9') c_ = c;
  }
  void initMap() {
    for(auto p: h) {
      assert(!m.count(p.first));
      m[p.first] = p.second;
      if (p.first == p.second) continue;
      assert(!m.count(p.second));
      m[p.second] = p.first;
    }
  }
  UpsideType& getUpside() {
    if (!m.size()) initMap();
    if (p) delete p;
    p = new UpsideDigit(m.count(c_) ? m[c_] : invalid);
    return *p;
  }
  bool equal(UpsideType& f) {
    if (typeid(f) != typeid(*this)) return false;
    UpsideDigit& ff = static_cast<UpsideDigit&>(f);
    if (!valid() || !ff.valid()) return false;
    return c_ == ff.c_;
  }
};
const vector<UpsideDigit::pairchar> UpsideDigit::h =
   {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}};

typedef vector<UpsideRef> StringUs;
typedef vector<UpsideLC> StringLC;
typedef vector<UpsideDigit> StringDigit;

std::ostream& operator<<(std::ostream& out, const StringUs& str) {
  for(UpsideType& c: str) c.print();
  return out;
}

class DictUs {
public:
  virtual StringUs getWord(int index) = 0;
};

class DictLC : public DictUs {
public:
  DictLC(initializer_list<string> list) {
    for(auto l : list) {
      StringLC str(l.begin(), l.end());
      strs.emplace_back(str);
    }
  }

  StringUs getWord(int index) {
    if (index >= strs.size()) return {};
    StringUs ret;
    for(UpsideLC &g: strs[index]) ret.push_back(g);
    return ret;
  }
private:
  vector<StringLC> strs;
};

class DictDigit : public DictUs {
public:
  DictDigit(initializer_list<string> list) {
    for(auto l : list) {
      StringDigit str(l.begin(), l.end());
      strs.emplace_back(str);
    }
  }

  StringUs getWord(int index) {
    if (index >= strs.size()) return {};
    StringUs ret;
    for(UpsideDigit &g: strs[index]) ret.push_back(g);
    return ret;
  }
private:
  vector<StringDigit> strs;
};

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

class UpsideUs {
public:
  UpsideUs() { }

  vector<StringUs> allUpSide(DictUs& dict) {
    vector<StringUs> r;
    for(int i = 0; ; ++i) {
        StringUs s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSide(s)) r.emplace_back(s);
    }
    return r;
  }

  bool isUpSide(const StringUs &s) {
    int n = s.size(), nn = (n+1)/2;
    for (int i = 0; i < nn; ++i) {
        UpsideType &c = s[i];
        UpsideType &cc = c.getUpside();
        UpsideType &d = s[n-i-1];
        if (!cc.valid() || d != cc) return false;
    }
    return true;
  }
};

class Upside2Us : public UpsideUs {
public:
  Upside2Us() : UpsideUs() { }
  vector<StringUs> allUpSideDiff(DictUs& dict) {
    vector<StringUs> r;
    for(int i = 0; ; ++i) {
        StringUs s = dict.getWord(i);
        if (s.empty()) break;
        if (isUpSideDiff(s)) r.emplace_back(s);
    }
    return r;
  }
  bool isUpSideDiff(const StringUs &s) {
      int n = s.size(), nn = (n+1)/2;
      bool f = false;
      for (int i = 0; i < nn; ++i) {
          UpsideType &c = s[i];
          UpsideType &d = s[n-i-1];
          UpsideType &cc = c.getUpside();
          UpsideType &dd = d.getUpside();
          if (!cc.valid() || !dd.valid()) return false;
          if (cc != d) f = true;
      }
      return f;
  }
};

int main(int argc, char **argv) {
  UpsideLC ca('a'), ce('e');
  UpsideRef ref1 = ca, ref2 = ce;
  if (ca == ce) cout << "same0" << endl;
  else cout << "diff0" << endl;
  if (ref1.get() == ref2.get()) cout << "same1" << endl;
  else cout << "diff1" << endl;
  UpsideType& ref = ca.getUpside();
  if (ce == ref) cout << "same2" << endl;
  else cout << "diff2" << endl;

  DictLC dictLC = { "axe", "dip", "dollop", "mow", "hello", "omw" };
  UpsideUs usus;
  vector<StringUs> resultus = usus.allUpSide(dictLC);
  for(auto s: resultus) cout << s << " "; cout << endl;

  Upside2Us usus2;
  vector<StringUs> resultus2 = usus2.allUpSideDiff(dictLC);
  for(auto s: resultus2) cout << s << " "; cout << endl;

  DictDigit dictDigit = { "123", "121", "696", "689", "081", "152", "101", "6699", "969", "1221", "888" };
  resultus = usus.allUpSide(dictDigit);
  for(auto s: resultus) cout << s << " "; cout << endl;

  resultus2 = usus2.allUpSideDiff(dictDigit);
  for(auto s: resultus2) cout << s << " "; cout << endl;

  return 0;
}

