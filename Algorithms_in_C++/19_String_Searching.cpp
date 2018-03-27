
// 1. kurt-morris-pratt algorithm by reuse the match part and increase i
// 2. boyer-moore algorithm by comparing the tail string first and increase i 
// 3. Rabin-Karp algorithm by hash value from polymid and prime

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
    getNext(pattern, result, improve);
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

// index = i means N-1 ~ N-i+1 match but N-i mismatch
void getNext2(string &pattern, vector<int> &result)
{
    int n = pattern.size();
    result.resize(n+2, 0);
    for(int i = 1; i <= (n+1); i++)
    {
        int k = i-1;
	for(int j = n-1; j > 0; j--) // use the first j characters
	{
	    int len = (j < k) ? j : k;	
	    if (pattern.substr(j-len, len) == pattern.substr(n-len, len))
		if (pattern[n-i] != pattern[j-i])     
		{  result[i] = n-j; break; }
	}
    }

    for(int i = 0; i < result.size(); i++) cout << result[i] << " ";
    cout << endl;   
}

void findPattern2(string &example, string &pattern, vector<int> &find)
{
    vector<int> result;
    getNext2(pattern, result);

    int i = 0;
    int j = 0;
    int n = pattern.size();
    for(i = n-1, j = n-1; i < example.size(); i--, j--)
    {
        int k = n-j;
        if (j < 0) 
	{ 
	    find.emplace_back(i+1); 
	    i += (k+result[k]);
	    j = n;
	    continue;
	}

	if (example[i] != pattern[j]) 
	{
	    //cout << i << " " << j << endl;	
	    i += (k+result[k]);
	    j = n;
	}
    }
   
    cout << example << "=";
    for(int i = 0; i < find.size(); i++) cout << find[i] << " ";
    cout << endl;
}

// string => hash by A0*D^M-1+A1*D^M-2+AM-1 % prime number
#define ctoi(c) (int)((c)-'0'+1)
void findPattern3(string &example, string &pattern, vector<int> &find)
{
    int p = 104729;    	
    int d = 3; // shall be more than the value from ctoi
    int hp = 0;
    int hh = 0; 
    int plen = pattern.size();
    int elen = example.size();
    int dd = 1;

    for(int i = 0; i < plen; i++)
    {
        hp = (hp*d + ctoi(pattern[i])) % p;
	hh = (hh*d + ctoi(example[i])) % p;
    }

    int i = 0;
    int n = elen - plen;
    for(int i = 1; i < plen; i++) dd = (dd*d) %p; 
    for(i = 0; i < n; i++)
    {
        if (hp == hh) // && example.substr(i, plen) == pattern)
	    find.emplace_back(i);
	hh = (hh + d*p - ctoi(example[i])*dd) %p;
	hh = (hh*d + ctoi(example[i+plen])) %p;
    }

    if (hp == hh) // && example.substr(i, plen) == pattern)
       find.emplace_back(i);
    
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
    cout << "=====================" << endl;
    string pattern2 = "10110101";
    vector<int> result;
    getNext2(pattern2, result);    
    find.clear();
    findPattern2(example0, pattern, find);
    find.clear();
    findPattern2(example1, pattern, find);
    find.clear();
    findPattern2(example2, pattern, find);
    find.clear();
    findPattern2(example3, pattern, find);
    cout << "=====================" << endl;
    find.clear();
    findPattern3(example0, pattern, find);
    find.clear();
    findPattern3(example1, pattern, find);
    find.clear();
    findPattern3(example2, pattern, find);
    find.clear();
    findPattern3(example3, pattern, find);
    return 0;
}
