
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    stack<string> mystack;

    mystack.emplace("First Sentence");
    mystack.push("interrupt");
    mystack.emplace("Second Sentence");

    cout << "mystack contains:\n";
    while(!mystack.empty())
    {
        cout << mystack.top() << "\n";
	mystack.pop();
    }

    return 0;
}
