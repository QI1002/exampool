
#include <list>
#include <string>
#include <vector>
#include <time.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
class Solution {
private:
    string t;
    bool debug = false;
public:
    void log(bool f) { debug = f; }
    void set(string& target) { t = target; }
    void guess(string& s) {
	int n = s.length();
        if (n != t.length()) return;
	for(int i = 0; i < n; i++)
	    if (s[i] != t[i]) s[i] = '?';
    }
    string answer(int n) {
   	int i, j, count = 0;
	string s(n, '?'); list<int> h;
        for(i = 0; i < n; i++) h.emplace_back(i);
	for(char c = 'a'; c <= 'z' && h.size() > 0; c++) {
	    string g(n, c); guess(g); count++; 
	    for(auto it = h.begin(); it != h.end(); ) {
		j = *it;
                if (g[j] != c) { ++it; continue; } 
		s[j] = c; it = h.erase(it);		
	    }
	}

	if (t == s) { 
	    if (debug) cout << t << " guess success with cnt = " << count << endl;
	}else 	    
	    cout << t << " guess failure by " << s << " with cnt = " << count << endl;    
        return s;
    }	    
};

#define MAX_LIMIT 500
int main(int argc, char* argv[]) {
    Solution s;
    srand(time(NULL));
    int i, j = 1, len; string t;
    if (argc > 2 || argc == 1) 
	cout << argv[0] << " usage: " << argv[0] << " {test_count|test_pattern}" << endl;
    else {
	try {
	    s.log(true); j = stoi(argv[1]);
	}catch(exception e) {
            s.log(false); t = argv[1]; 		
	}
        for(; j > 0; j--) {
	    if (t.length()) { s.set(t); s.answer(t.length()); continue; }
            len = (rand() % MAX_LIMIT) + 1;
            for(int i = 0; i < len; i++) t += static_cast<char>((rand() % 26) + 'a'); 
            s.set(t); s.answer(len); t = "";
        }
    }
    return 0;
}
