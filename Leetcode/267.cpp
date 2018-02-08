

// 266. Palindrome Permutation II
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <map>

using namespace std;
typedef map<char, int> charfreq;
typedef vector<string> stringarray;

void getFreq(string ss, charfreq& freq)
{
    for(int i=0; i < ss.length() ; i++)
    {
        char c = ss[i];
	if (freq.find(c) == freq.end())
	    freq[c] = 0;    
        freq[c] += 1;
    }
}

void getPerm(charfreq freq, stringarray& result)
{
    stack<string> s;
    int count = 0;
    for (charfreq::iterator iter = freq.begin();
         iter != freq.end(); iter++)
        count += iter->second;

    //cout << "sum count = " << count << "\n";
    s.push("");
    while(!s.empty())
    {
        string sp = s.top();
	s.pop();
	if (sp.length() == count)
	{
	    result.push_back(sp);
	    continue;
	}
	 
	charfreq p;
	getFreq(sp, p);

        for (charfreq::iterator iter = freq.begin();
             iter != freq.end(); iter++)
	{
            int f = iter->second;
	    if (p.find(iter->first) != p.end())
		f -= p[iter->first];
            if (f > 0) s.push(sp + iter->first);
	}
    }
}

void allPalPerm(string ss, stringarray& result)
{
    charfreq freq;
    getFreq(ss, freq);

    string odd = "";
    for (charfreq::iterator iter = freq.begin();
         iter != freq.end(); iter++)
    {
	int f = iter->second;
	if ((f % 2) == 1)
	{
            if (odd == "") odd = iter->first; 
            else return;
	}
    }

    if (odd != "") freq.erase(freq.find(odd[0]));
    for (charfreq::iterator iter = freq.begin();
         iter != freq.end(); iter++)
        iter->second /= 2;

    stringarray ssl;
    getPerm(freq, ssl);
    for (stringarray::iterator iter = ssl.begin();
         iter != ssl.end(); iter++)
    {
	string rev(iter->rbegin(), iter->rend());    
        string sl = *iter + odd + rev;
	result.push_back(sl);	
    }
}

void test(string ss)
{
    stringarray result;	
    allPalPerm(ss, result);
    cout << "\"" << ss << "\" total = " << result.size() << "\n";
    for (stringarray::iterator iter = result.begin();
         iter != result.end(); iter++)
        cout << *iter << endl; 
}

void test2()
{
    charfreq freq;
    stringarray result;

    freq['a'] = 1;
    freq['b'] = 2;
    freq['c'] = 3;
    getPerm(freq, result);
    cout << "total = " << result.size() << "\n";
    for (stringarray::iterator iter = result.begin();
         iter != result.end(); iter++)
        cout << *iter << endl; 
}

int main()
{
#if 1 
    test("code");
    test("aab");
    test("carerac");
    test("ccaaeaacc");
#else
    test2();
#endif

    return 0;
}
