
//
//
//
#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

bool linkHash(int cap, vector<vector<char>> &h, string &example, vector<int> &result)
{
    for(int i = 0; i < example.size(); i++)
    {
        char c = example[i];
        int value = c - 'A' + 1;
	int hash = value % cap;

        h[hash].emplace_back(c);
	result[i] = hash;
    }
}

bool linearHash(int cap, vector<char> &h, string &example, vector<tuple<int,int>> &result)
{
    for(int i = 0; i < example.size(); i++)
    {
        char c = example[i];
        int value = c - 'A' + 1;
	int hash = value % cap;
	int index = -1;
	for(int j = 0; j < h.size(); j++)
	{
	    int slot = ((hash+j) < h.size()) ? hash+j : hash+j-h.size();
            if (h[slot] == -1) { index = slot; break; }   
	}

	if (index == -1) return false;
	result[i] = tuple<int, int>(hash, index);
	h[index] = c;
    }

    return true;
}

bool doubleHash(int cap, int cap2, vector<char> &h, string &example, vector<tuple<int,int,int>> &result)
{
    for(int i = 0; i < example.size(); i++)
    {
        char c = example[i];
        int value = c - 'A' + 1;
	int hash1 = value % cap;
	int hash2 = cap2 - (value % cap2);
	int index = -1;
	for(int j = 0; j < h.size(); j++)
	{
	    int slot = (hash1+j*hash2) % cap;
            if (h[slot] == -1) { index = slot; break; }   
	}

	if (index == -1) return false;
	result[i] = tuple<int, int, int>(hash1, hash2, index);
	h[index] = c;
    }

    return true;
}

int main(int argc, char* argv[])
{
    string example = "ASEARCHINGEXAMPLE";
    int cap = 19;
    int cap2 = 8;
    int cap3 = 11;
    vector<char> hash1(cap, -1);
    vector<char> hash2(cap, -1);
    vector<vector<char>> hash3(cap3);

    cout << "====================================" << endl;
    vector<tuple<int,int>> result(example.size());
    linearHash(cap, hash1, example, result);
    for(int i = 0; i < hash1.size(); i++) cout << hash1[i] << ","; 
    cout << endl;
    for(int i = 0; i < result.size(); i++) cout << get<0>(result[i]) << ","; 
    cout << endl;
    for(int i = 0; i < result.size(); i++) cout << get<1>(result[i]) << ","; 
    cout << endl;

    cout << "====================================" << endl;
    vector<tuple<int,int,int>> result2(example.size());
    doubleHash(cap, cap2, hash2, example, result2);
    for(int i = 0; i < hash2.size(); i++) cout << hash2[i] << ","; 
    cout << endl;
    for(int i = 0; i < result2.size(); i++) cout << get<0>(result2[i]) << ","; 
    cout << endl;
    for(int i = 0; i < result2.size(); i++) cout << get<1>(result2[i]) << ","; 
    cout << endl;
    for(int i = 0; i < result2.size(); i++) cout << get<2>(result2[i]) << ","; 
    cout << endl;
   
    cout << "====================================" << endl;
    vector<int> result3(example.size());
    linkHash(cap3, hash3, example, result3);
    for(int i = 0; i < hash3.size(); i++) 
    {
        cout << i << ":";	    
	for(int j = 0; j < hash3[i].size(); j++) cout << hash3[i][j] << ","; 
        cout << endl;
    }
    for(int i = 0; i < result3.size(); i++) cout << result3[i] << ","; 
    cout << endl;
    return 0;
}
