
#include <iostream>
#include <vector>
#include <queue>
#include <math.h>
#include <time.h>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

int swap(vector<int> &s, int a, int b)
{
    int tmp = s[a];
    s[a] = s[b];
    s[b] = tmp;
}

void qsort(vector<int> &s, int l = -1, int r = -1)
{
    if (l == -1) l = 0;
    if (r == -1) r = s.size()-1;
    if (l >= r) return;

    int i = l-1;
    int j = r;
    int a = s[r];

    while(true)
    {
        while(s[++i] < a);
        while(i < j && s[--j] > a);    
        if (i >= j) break;
        swap(s, i, j);
    }

    //cout << i << ":" << j << endl;
    swap(s, i, r);
    qsort(s, l, i-1);
    qsort(s, i+1, r);
}
 
void upheap(vector<int> &s, int t)
{
    s.emplace_back(t);
    int n = s.size()-1;
    while(n != 0 && s[n/2] > s[n]) { swap(s, n/2, n); n = n/2; } 
}

int downheap(vector<int> &s)
{
    if (s.size() < 2) return -1;

    int i = 1;
    int rr = s[i];
    swap(s, i, s.size()-1);
    s.pop_back();
    
    while(true)
    {
        int l = i*2; int r = l+1; int j = i;
        if (r < s.size() && s[r] < s[l]) j = r; 
        else if (l < s.size()) j = l;  
        if (i == j) break;
        if (s[j] < s[i]) swap(s, i, j);
        i = j; 
    }

    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    return rr;   
}

int heapsort(vector<int> &s)
{
    vector<int> t;
    t.insert(t.begin(), -1);
    int n = s.size();
    for(int i = 0; i < n; i++) upheap(t, s[i]); 
    s.clear();
    for(int i = 0; i < n; i++) s.emplace_back(downheap(t));
}

class icomp
{
public:
    bool operator()(const int &a, const int &b) { return a > b; }
};

int heapsort2(vector<int> &s)
{
    priority_queue<int, vector<int>, icomp> t;
    int n = s.size();
    for(int i = 0; i < n; i++) t.push(s[i]); 
    s.clear();
    for(int i = 0; i < n; i++) { s.emplace_back(t.top()); t.pop(); }
}

int bsearch(vector<int> &s, int t)
{
    int l = 0; 
    int r = s.size()-1;
    int m;
    
    while(l<=r)
    {
        m = (l+r)/2;
        if (s[m] == t) return m;
        if (s[m] < t) l = m+1;
        else r = m-1;  
    } 

    return (s[m] < t) ? m+1 : m;
}

int main(int argc, char* argv[])
{
    int sample[] = { 1, 3, 6, 10, 15, 21, 30, 37 };    
    int test[] = { -1, 1, 2, 3, 4, 6, 8, 10, 13, 15, 18, 21, 25, 30, 33, 37, 40};
    vector<int> s;
    s.assign(sample, sample+ELEMOF(sample));
    for (int i = 0; i < ELEMOF(test); i++) 
        cout << test[i] << ":" << bsearch(s, test[i]) << endl;

    cout << "==================================" << endl;
    int sample1[] = { 1, 3, 6, 10, 15, 21, 30, 37 };    
    int sample2[] = { 37, 30, 21, 15, 10, 6, 3, 1 };
    s.assign(sample1, sample1+ELEMOF(sample1)); qsort(s);
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    s.assign(sample2, sample2+ELEMOF(sample2)); qsort(s);
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    
    cout << "==================================" << endl;
    srand((unsigned int)time(NULL)); vector<int> ss = s; s.clear(); int n = ss.size();
    for (int i = n; i > 1; i--) 
    { int j = rand()%i; s.emplace_back(ss[j]); auto it = ss.begin()+j; ss.erase(it); }
    s.emplace_back(ss[0]); 
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    qsort(s);
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;

    cout << "==================================" << endl;
    srand((unsigned int)time(NULL)); ss = s; s.clear(); n = ss.size();
    for (int i = n; i > 1; i--) 
    { int j = rand()%i; s.emplace_back(ss[j]); auto it = ss.begin()+j; ss.erase(it); }
    s.emplace_back(ss[0]); 
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    heapsort2(s);
    for (int i = 0; i < s.size(); i++) cout << s[i] << ","; cout << endl;
    
    return 0;
}

