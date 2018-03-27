
//
//
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void getNext(string &pattern, vector<int> &result, bool improve = true)
{
    result.resize(pattern.size(), 0);
    for(int i = 1; i < pattern.size(); i++)
    {
        int j = 0;
	while((i+j) < pattern.size() && pattern[i+j] == pattern[j])
	{	
	    j++;
	    if ((i+j) < pattern.size() && result[i+j] < j) result[i+j] = j;
	}
    }

    result[0] = -1;
    if (improve == false) return;
    for(int i = 1; i < pattern.size(); i++)
    {
	int j = result[i];    
        while( j >= 0 && pattern[i] == pattern[j]) j = result[j];
	result[i] = j;
    }
}

void findPattern(string &example, string &pattern, vector<int> &find, bool improve = true)
{
    vector<int> result;
    getNext(pattern, result, true);
    for(int i = 0; i < result.size(); i++) cout << result[i] << " ";
    cout << endl;   

    int n = example.size();
    int j = 0;
    for(int i = 0; i < n; i++)
    {
	cout << i << " " << j << endl;
	if (j == pattern.size()) { find.emplace_back(i-j); j = 0; break; }    
#if 1
	while(example[i] != pattern[j])
	{
            j = result[j];
	    if (j == -1) break;
	}

	j++;
#else
	if (example[i] == pattern[j]) { j++; continue; }
        else 
	{
	    bool match = false;
	    while(result[j] != -1)
	    {
                j = result[j];
	        if (pattern[j] == example[i]) { match = true; j++; break; } 
	    }
	    
	    if (match == false) j = 0;
	}
#endif
    }
}

int main(int argc, char* argv[])
{
    string example = "100111010010100010100111000111";
    string pattern = "10100111";

    vector<int> find;
    findPattern(example, pattern, find);
    for(int i = 0; i < find.size(); i++) cout << find[i] << " ";
    cout << endl;
    return 0;
}
