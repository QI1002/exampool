
#include <iostream>
#include <stack>

using namespace std;

int main(void)
{
    char c;
    stack<char> save;
    
    while(cin.get(c))
    {
        if (c == ')') 
	{
	    cout.put(save.top());
	    save.pop();
	}

	if (c == '+') save.push(c); 
	if (c == '*') save.push(c); 
        while(c >= '0' && c <= '9')
	{
            cout.put(c);
	    cin.get(c);
	}

	if (c!= '(') cout << ' ';
    }

    return 0;
} 
