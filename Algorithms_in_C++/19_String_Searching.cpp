
//
//
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void getNext(string &pattern, vector<int> &result, bool improve = true)
{
    result.resize(pattern.size()+1, 0);
    for(int i = 1; i < pattern.size(); i++)
    {
        int j = 0;
	while((i+j) < pattern.size() && pattern[i+j] == pattern[j])
	{	
	    j++; // it's important to use increaed j for next statement
	    if (result[i+j] < j) result[i+j] = j;
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

    int i = 0;
    int j = 0;
    for(i = 0; i < example.size(); i++)
    {
	//cout << i << " " << j << endl;
	if (j == pattern.size()) { find.emplace_back(i-j); j = result[j]; }    
	while(example[i] != pattern[j])
	{
            j = result[j];
	    if (j == -1) break;
	}

	j++; // it also works for -1 to 0  
    }

    if (j == pattern.size()) find.emplace_back(i-j);
   
    cout << example << "=";
    for(int i = 0; i < find.size(); i++) cout << find[i] << " ";
    cout << endl;
}

int main(int argc, char* argv[])
{
    string example0 = "100111010010100010100101000111";
    string example1 = "100111010010100010100111000111";
    string example2 = "1001110100101000101001110100111";
    string example3 = "1001110100111000101001010100111";
    string pattern = "10100111";

    vector<int> find;
    findPattern(example0, pattern, find);
    find.clear();
    findPattern(example1, pattern, find);
    find.clear();
    findPattern(example2, pattern, find);
    find.clear();
    findPattern(example3, pattern, find);
    return 0;
}
