
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
  virtual UpsideType* getUpside() = 0;
  virtual bool equal(UpsideType* p) = 0;
  bool operator==(UpsideType& f) { return equal(&f); }
  bool operator!=(UpsideType& f) { return !equal(&f); }
  bool valid() { return c_ != invalid; }
  void print() { cout << c_; }
};
const char UpsideType::invalid;


class UpsideLC : public UpsideType {
 private:
  static const vector<pairchar> h;
 public:
  UpsideLC(const char &c) {
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
  UpsideType* getUpside() {
    if (!m.size()) initMap();
    if (!m.count(c_)) return NULL;
    return new UpsideLC(m[c_]);
  }
  bool equal(UpsideType* p) {
    if (p == NULL) return false;
    if (typeid(*p) != typeid(*this)) return false;
    UpsideLC* pt = static_cast<UpsideLC*>(p);
    if (!valid() || !pt->valid()) return false;
    return c_ == pt->c_;
  }
};
const vector<UpsideLC::pairchar> UpsideLC::h =
   {{'a', 'e'}, {'b', 'q'}, {'d', 'p'}, {'f', 't'}, {'h', 'y'}, {'i', 'i'},
    {'l', 'l'}, {'m', 'w'}, {'n', 'u'}, {'o', 'o'}, {'s', 's'}, {'x', 'x'}, {'z','z'}};

class UpsideDigit : public UpsideType {
 private:
  static const vector<pairchar> h;
 public:
  UpsideDigit(const char &c) {
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
  UpsideType* getUpside() {
    if (!m.size()) initMap();
    if (!m.count(c_)) return NULL;
    return new UpsideDigit(m[c_]);
  }
  bool equal(UpsideType* p) {
    if (p == NULL) return false;
    if (typeid(*p) != typeid(*this)) return false;
    UpsideDigit* pt = static_cast<UpsideDigit*>(p);
    if (!valid() || !pt->valid()) return false;
    return c_ == pt->c_;
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
        shared_ptr<UpsideType> p(c.getUpside());
        UpsideType &d = s[n-i-1];
        if (!d.equal(p.get())) return false;
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
          shared_ptr<UpsideType> p(c.getUpside());
          shared_ptr<UpsideType> q(d.getUpside());
          if (p.get() == NULL || q.get() == NULL) return false;
          if (!d.equal(p.get())) f = true;
      }
      return f;
  }
};

int main(int argc, char **argv) {
  UpsideLC ca('a'), ce('e');
  UpsideType *p1 = &ca, *p2 = &ce;
  if (ca == ce) cout << "same0" << endl;
  else cout << "diff0" << endl;
  if (*p1 == *p2) cout << "same1" << endl;
  else cout << "diff1" << endl;
  shared_ptr<UpsideType> p(ca.getUpside());
  if (p) {
    if (ce == *p) cout << "same2" << endl;
    else cout << "diff2" << endl;
  } else {
    cout << "upside2 fail" << endl;
  }

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

