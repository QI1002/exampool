
#include <iostream>
#include <string>
#include <stack>
#include <deque>

using namespace std;

template<typename T>
void show(T& t, string title)
{
    cout << title << " contains: " << t.size() << "\n";
    for (auto it = t.begin(); it != t.end(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void showr(T& t, string title)
{
    cout << title << " contains: " << t.size() << "\n";
    for (auto it = t.rbegin(); it != t.rend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void showc(T& t, string title)
{
    cout << title << " contains: " << t.size() << "\n";
    for (auto it = t.cbegin(); it != t.cend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void showcr(T& t, string title)
{
    cout << title << " contains: " << t.size() << "\n";
    for (auto it = t.crbegin(); it != t.crend(); it++)
	cout << *it << " ";
    cout << endl;
}

template<typename T>
void newshow(T& t, string title)
{
    cout << title << " contains(2): " << t.size() << "\n";
    for (auto& x: t) cout << x << " ";
    cout << endl;
}

void demostring()
{

}

void demovector()
{

}

void demomap()
{

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
    
    cout << "stack1 contains: " << stack1.size() << "\n";
    while(!stack1.empty())
    {
        cout << stack1.top() << "\n";
	stack1.pop();
    }

    cout << "stack2 contains: " << stack2.size() << "\n";
    while(!stack2.empty())
    {
        cout << stack2.top() << "\n";
	stack2.pop();
    }
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
    show<deque<int>>(deque2, "deque2");

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

int main(int argc, char* argv[])
{
    if (argc != 2) 
    {
        cout << "Usage: " << argv[0] << " [string|vector|map|stack|deque]";
        return 0;
    }

    if (string(argv[1]) == "string")
	demostring();

    if (string(argv[1]) == "vecotr")
	demovector();

    if (string(argv[1]) == "map")
	demomap();

    if (string(argv[1]) == "stack")
	demostack();

    if (string(argv[1]) == "deque")
	demodeque();
    
    return 0;
}
