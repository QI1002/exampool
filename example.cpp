
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <deque>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

template<typename T>
void show(T& t, string title)
{
    cout << title << " contains: " << t.size() << endl;
    for (auto it = t.begin(); it != t.end(); it++)
	cout << *it << " ";
    cout << endl;
}


template<typename T>
void showr(T& t, string title)
{
    cout << title << " contains(r): " << t.size() << endl;
    for (auto it = t.rbegin(); it != t.rend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void showc(T& t, string title)
{
    cout << title << " contains(c): " << t.size() << endl;
    for (auto it = t.cbegin(); it != t.cend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void showcr(T& t, string title)
{
    cout << title << " contains(cr): " << t.size() << endl;
    for (auto it = t.crbegin(); it != t.crend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void newshow(T& t, string title)
{
    cout << title << " contains(2): " << t.size() << endl;
    for (auto& x: t) cout << x << " ";
    cout << endl;
}

template<typename T>
void showmap(T& t, string title)
{
    cout << title << " contains: " << t.size() << endl;
    for (auto it = t.begin(); it != t.end(); it++)
	cout << "(" << it->first << "," << it->second << ") ";
    cout << endl;
}

template<typename T>
void showmapr(T& t, string title)
{
    cout << title << " contains(r): " << t.size() << endl;
    for (auto it = t.rbegin(); it != t.rend(); it++)
	cout << "(" << it->first << "," << it->second << ") ";
    cout << endl;
}

template<typename T>
void showmapc(T& t, string title)
{
    cout << title << " contains(c): " << t.size() << endl;
    for (auto it = t.cbegin(); it != t.cend(); it++)
	cout << "(" << it->first << "," << it->second << ") ";
    cout << endl;
}

template<typename T>
void showmapcr(T& t, string title)
{
    cout << title << " contains: " << t.size() << endl;
    for (auto it = t.crbegin(); it != t.crend(); it++)
	cout << "(" << it->first << "," << it->second << ") ";
    cout << endl;
}

template<typename T>
void newshowmap(T& t, string title)
{
    cout << title << " contains(2): " << t.size() << endl;
    for (auto& x: t)
	cout << "(" << x.first << "," << x.second << ") ";
    cout << endl;
}

template<typename T>
void display(T& t, string title)
{
    cout << title << " contains: " << t.size() << endl;
    while(!t.empty())
    {
        cout << t.top() << " ";
	t.pop();
    }

    cout << endl;
}

template<typename T>
void display2(T& t, string title)
{
    cout << title << " contains: " << t.size() << endl;
    cout << title << " back is " << t.back() << endl;
    while(!t.empty())
    {
        cout << t.front() << " ";
	t.pop();
    }

    cout << endl;
}

void demostring()
{
    char buf[20];
    string str = "This is a Miracle";

    cout << "find " << str << " with is:" << str.find("is") << endl;
    cout << "find " << str << " with is:" << str.rfind("is") << endl;
    
    size_t sz = str.copy(buf, str.length(), 0);
    buf[sz] = 0;

    cout << "partial of string: " << buf << endl;

    char c = '0';
    sz = str.find_first_of("iaeou");
    while (sz != string::npos) 
    {
        str[sz] = c++;
	sz = str.find_first_of("iaeou");
    }

    cout << "update vowel from head: " << str << endl;

    str = buf;
    c = '0';
    sz = str.find_last_of("iaeou");
    while (sz != string::npos) 
    {
        str[sz] = c++;
	sz = str.find_last_of("iaeou");
    }

    cout << "update vowel from tail: " << str << endl;

    str = buf;
    c = '0';
    sz = str.find_first_not_of("iaeou");
    while (sz != string::npos) 
    {
        str[sz] = c++;
	sz = str.find_first_not_of("iaeou", sz+1);
    }

    cout << "update consonant from head: " << str << endl;

    str = buf;
    c = '0';
    sz = str.find_last_not_of("iaeou");
    while (sz != string::npos) 
    {
        str[sz] = c++;
	sz = str.substr(0, sz).find_last_not_of("iaeou");
    }

    cout << "update consonant from tail: " << str << endl;
    string result = (str.compare(buf) > 0) ? "new > old" : "old > new";    
    cout << "compare result: " << result << endl;

    string newstr(buf);
    str.swap(newstr);
    str.replace(2, 10, "at is an o");
    cout << "replaced string: " << str << endl;
    
    str = buf;
    str.erase(4, 3);
    cout << "erased string: " << str << endl;
    str.erase(str.cbegin()+4, str.cend());
    cout << "erased string: " << str << endl;

    str.shrink_to_fit();
}

void demovector()
{
    vector<int> vector1 = {10, 20, 30};
    vector<int> vector2;

    auto it = vector1.emplace(vector1.begin()+1, 100);
    vector1.emplace(it, 200);
    vector1.emplace_back(1000);

    cout << vector1.back() << endl;
    show<vector<int>>(vector1, "vector1");
    showr<vector<int>>(vector1, "vector1");
    
    vector2.assign(7, 11);
    showc<vector<int>>(vector2, "vector2");

    vector2.assign(vector1.cbegin()+1, vector1.cend()-1);
    show<vector<int>>(vector2, "vector2");

    const int v[] = {111,222,333,444};
    vector2.assign(v, v+4);
    show<vector<int>>(vector2, "vector2");
    vector2.insert(vector2.end(), vector1.cbegin()+1, vector1.cend()-1);
    newshow<vector<int>>(vector2, "vector2");

    vector1.pop_back();
    vector1.push_back(2000);
    newshow<vector<int>>(vector1, "vector1");

    cout << "max size = " << vector2.max_size() << endl;
    vector2.erase(vector2.cbegin(), vector2.cbegin()+4);
    newshow<vector<int>>(vector2, "vector2");

    vector1.swap(vector2);
    newshow<vector<int>>(vector2, "vector2");

    vector2.resize(5);
    vector2.resize(7, 99);
    int* p = vector2.data(); p[6] = 999;
    showcr<vector<int>>(vector2, "vector2");

    vector2.clear();
    newshow<vector<int>>(vector2, "vector2");
    cout << "vector2 is empty: " << vector2.empty() << endl;
    vector2.shrink_to_fit();

}

char* itoa10(int i)
{
    static char buf[5];
    return itoa(10*i, buf, 10);
}

void demomap()
{
    map<int, string> map1;
    map<int, string> map2;
    int highkey = 3;
    pair<int, string> highpair = pair<int, string>(4, itoa10(4));   

    map<int, string>::key_compare kcomp = map1.key_comp();
    map<int, string>::value_compare vcomp = map1.value_comp();
    for (int i = 0; i <= 5; i++) map1.insert(pair<int, string>(i, itoa10(i)));

    auto p = map1.insert(pair<int, string>(5, itoa10(5)));
    cout << "result = " << p.second << " with " << p.first->first << "," << p.first->second << endl;
    p = map1.emplace(pair<int, string>(6, itoa10(6)));
    cout << "result = " << p.second << " with " << p.first->first << "," << p.first->second << endl;
    auto itt = map1.emplace_hint(p.first, pair<int, string>(7, itoa10(7)));
    cout << "hit emplace: " << itt->first << "," << itt->second << endl;
    showmap<map<int, string>>(map1, "map1");
 
    cout << "map1 key less than " << highkey << ": ";
    auto it1 = map1.begin();
    while (kcomp(it1->first, highkey))
    {
	cout << "(" << it1->first << "," << it1->second << ") ";
	it1++;
    }
    cout << endl;

    cout << "map1 value less than (" << highpair.first << "," << highpair.second << "): "; 
    auto it2 = map1.begin();
    while (vcomp(*it2, highpair))
    {
	cout << "(" << it2->first << "," << it2->second << ") ";
	it2++;
    }
    cout << endl;

    map1.erase(0);
    map1.erase(map1.find(7));
    itt = map1.find(7);
    if (itt == map1.end())
        cout << "find 7: not found" << endl;
    else
	cout << "find 7 (" << itt->first << "," << itt->second << ") " << endl;
    cout << "count 6:" << map1.count(6) << " count 7:" << map1.count(7) << endl;
    auto ilower = map1.lower_bound(-1);
    auto iupper = map1.upper_bound(100);
    cout << "lower -1 (" << ilower->first << "," << ilower->second << ") " << endl;
    cout << "upper 100 (" << iupper->first << "," << iupper->second << ") " << endl;
    showmapr<map<int, string>>(map1, "map1");

    ilower++; iupper--; // no +1,-1 only ++ and --
    map2.insert(ilower, iupper);
    newshowmap<map<int, string>>(map2, "map2");

    map1.swap(map2);
    showmapc<map<int, string>>(map1, "map1");

    auto ret = map1.equal_range(3);
    cout << "lower (" << ret.first->first << "," << ret.first->second << ") " << endl;
    cout << "upper (" << ret.second->first << "," << ret.second->second << ") " << endl;

    map1.clear();
    showmap<map<int, string>>(map1, "map1");
    cout << "map1 is empty: " << map1.empty() << endl;
    //map1.shrink_to_fit();
}

void demostack()
{
    stack<string> stack1;
    stack<string> stack2;

    stack1.emplace("1st");
    stack1.push("2nd");
    stack1.emplace("3th");

    stack2.push("abc");
    stack2.emplace("xyz");
    stack2.emplace("mno");
    stack2.emplace("ghi");
   
    stack1.swap(stack2);
    display<stack<string>>(stack1, "stack1");
    display<stack<string>>(stack2, "stack2");
}

void demodeque()
{
    deque<int> deque1 = {10, 20, 30};
    deque<int> deque2;

    auto it = deque1.emplace(deque1.begin()+1, 100);
    deque1.emplace(it, 200);
    deque1.emplace_front(-1);
    deque1.emplace_back(1000);

    cout << deque1.front() << " " << deque1.back() << endl;
    show<deque<int>>(deque1, "deque1");
    showr<deque<int>>(deque1, "deque1");
    
    deque2.assign(7, 11);
    showc<deque<int>>(deque2, "deque2");

    deque2.assign(deque1.cbegin()+1, deque1.cend()-1);
    show<deque<int>>(deque2, "deque2");

    const int v[] = {111,222,333,444};
    deque2.assign(v, v+4);
    show<deque<int>>(deque2, "deque2");
    deque2.insert(deque2.end(), deque1.cbegin()+1, deque1.cend()-1);
    newshow<deque<int>>(deque2, "deque2");

    deque1.pop_back(); deque1.pop_front();
    deque1.push_back(2000); deque1.push_front(-2);
    newshow<deque<int>>(deque1, "deque1");

    cout << "max size = " << deque2.max_size() << endl;
    deque2.erase(deque2.cbegin(), deque2.cbegin()+4);
    newshow<deque<int>>(deque2, "deque2");

    deque1.swap(deque2);
    newshow<deque<int>>(deque2, "deque2");

    deque2.resize(5);
    deque2.resize(7, 99);
    showcr<deque<int>>(deque2, "deque2");

    deque2.clear();
    newshow<deque<int>>(deque2, "deque2");
    cout << "deque2 is empty: " << deque2.empty() << endl;
    deque2.shrink_to_fit();
}

void demoset()
{
    set<int> set1;
    set<int> set2;
    int highest = 3;

    set<int>::key_compare comp = set1.key_comp();
    for (int i = 0; i <= 5; i++) set1.insert(i);

    auto p = set1.insert(5);
    cout << "result = " << p.second << " with " << *(p.first) << endl;
    p = set1.emplace(6);
    cout << "result = " << p.second << " with " << *(p.first) << endl;
    auto itt = set1.emplace_hint(p.first, 7);
    cout << "hit emplace: " << *itt << endl;

    show<set<int>>(set1, "set1");

    cout << "set1 less than " << highest << ": ";
    auto it = set1.begin();
    while (comp(*(it), highest)) cout << *(it++) << ' ';
    cout << endl;

    set1.erase(0);
    set1.erase(set1.find(7));
    itt = set1.find(7);
    if (itt == set1.end())
        cout << "find 7: not found" << endl;
    else
        cout << "find 7:" << *itt << endl;
    cout << "count 6:" << set1.count(6) << " count 7:" << set1.count(7) << endl;
    auto ilower = set1.lower_bound(-1);
    auto iupper = set1.upper_bound(100);
    cout << "lower -1: " << *ilower << " upper 100: " << *iupper << endl;
    showr<set<int>>(set1, "set1");

    int sample[] = {11, 22, 33};
    set2.insert(sample, sample+3);
    ilower++; iupper--; // no +1,-1 only ++ and --
    set2.insert(ilower, iupper);
    newshow<set<int>>(set2, "set2");

    set1.swap(set2);
    showc<set<int>>(set1, "set1");

    set1.clear();
    show<set<int>>(set1, "set1");
    cout << "set1 is empty: " << set1.empty() << endl;
    //set1.shrink_to_fit();
}

void demoqueue()
{
    queue<string> queue1;
    queue<string> queue2;

    queue1.emplace("1st");
    queue1.push("2nd");
    queue1.emplace("3th");

    queue2.push("abc");
    queue2.emplace("xyz");
    queue2.emplace("mno");
    queue2.emplace("ghi");
   
    queue1.swap(queue2);
    display2<queue<string>>(queue1, "queue1");
    display2<queue<string>>(queue2, "queue2");
}

void demopriority_queue()
{
    priority_queue<string> priority_queue1;
    priority_queue<string> priority_queue2;

    priority_queue1.emplace("1st");
    priority_queue1.push("2nd");
    priority_queue1.emplace("3th");

    priority_queue2.push("abc");
    priority_queue2.emplace("xyz");
    priority_queue2.emplace("mno");
    priority_queue2.emplace("ghi");
   
    priority_queue1.swap(priority_queue2);
    display<priority_queue<string>>(priority_queue1, "priority_queue1");
    display<priority_queue<string>>(priority_queue2, "priority_queue2");
}

void checkbound(vector<int>& vec, int target, auto comp)
{
    auto ilower = lower_bound(vec.begin(), vec.end(), target, comp);
    auto iupper = upper_bound(vec.begin(), vec.end(), target, comp);
    if (ilower == iupper) ilower --;
    if ((ilower - vec.begin()) >= 0)
        cout << "the search for " << target << " lower bound " << *ilower << endl;
    else
        cout << "the search for " << target << " lower bound -Nan" << endl;
    if ((iupper - vec.end()) < 0)
        cout << "the search for " << target << " upper bound " << *iupper << endl;
    else
        cout << "the search for " << target << " upper bound Nan" << endl;
}

void demoalgo()
{
    static int ints[] = { 3, 11, 21, 5, 7, 17, 27, 23 };
    vector<int> vec(ints, ints+8);
    auto mycomp1 = [](int i,int j) { return i < j; };
    auto mycomp2 = [](int i,int j) { return i > j; };

    // indirect sorting
    vector<int> index = { 0, 1, 2, 3, 4, 5, 6, 7 };
    auto mycompi = [](int i, int j) { return ints[i] < ints[j]; };
    sort(index.begin(), index.end(), mycompi);
    show<vector<int>>(index, "index");

    sort(vec.begin(), vec.end(), mycomp2);
    show<vector<int>>(vec, "vec");

    sort(vec.begin(), vec.end(), mycomp1);
    show<vector<int>>(vec, "vec");

    int target = 5;
    if (binary_search(vec.begin(), vec.end(), target))
        cout << "the search for " << target << " successes" << endl; 
    else
        cout << "the search for " << target << " fails" << endl; 

    sort(vec.begin(), vec.end(), mycomp1);
    checkbound(vec, 11, mycomp1);
    checkbound(vec, 10, mycomp1);
    checkbound(vec, -1, mycomp1);
    checkbound(vec, 30, mycomp1);
    cout << "========================" << endl;
    sort(vec.begin(), vec.end(), mycomp2);
    checkbound(vec, 11, mycomp2);
    checkbound(vec, 10, mycomp2);
    checkbound(vec, -1, mycomp2);
    checkbound(vec, 30, mycomp2);
}

int main(int argc, char* argv[])
{
    if (argc != 2) 
    {
        cout << "Usage: " << argv[0] << " [string|vector|map|stack|deque|set|queue|priority_queue|algo]";
        return 0;
    }

    if (string(argv[1]) == "string")
	demostring();

    if (string(argv[1]) == "vector")
	demovector();

    if (string(argv[1]) == "map")
	demomap();

    if (string(argv[1]) == "stack")
	demostack();

    if (string(argv[1]) == "deque")
	demodeque();

    if (string(argv[1]) == "set")
	demoset();

    if (string(argv[1]) == "queue")
	demoqueue();

    if (string(argv[1]) == "priority_queue")
	demopriority_queue();

    if (string(argv[1]) == "algo")
	demoalgo();

    return 0;
}
