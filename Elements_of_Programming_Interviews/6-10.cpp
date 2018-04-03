
#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>

using namespace std;

void permGen(vector<int>& result, int k)
{
    vector<int> data(k);
    for(int i = 0; i < k; i++) data[i] = i;
    for(int i = k; i > 1; i--) 
    {
        int j = rand() % i;
	auto it = data.begin() + j;
	result.emplace_back(data[j]);
	data.erase(it);
    }

    result.emplace_back(data[0]);
}

void invertPerm(vector<int> &source, vector<int> &order)
{
    source.resize(order.size()); 
    for(int i = 0; i < order.size(); i++) 
	source[order[i]] = i;
}

int reorderbyPerm(vector<int> &data, vector<int> &order)
{
    vector<bool> check(data.size(), false);
    int count = 0;

    while(count < data.size())
    {		    
        int start;
        for(int j = 0; j < data.size(); j++) 
	    if (check[j] == false) { start = j; break; }	
        int i = start;
        int old = data[start];

        while(true)
        {
	    int j = order[i];
            count++;
	    check[i] = true;
	    if (j == start) { data[i] = old; break; }
            data[i] = data[j];
	    i = j;
        } 
    }

    return count; 
}

int main(int argc, char* argv[])
{
    int n = 11;
    vector<int> result;
    srand((unsigned int)time(NULL));
    permGen(result, n);
    for(int i = 0; i < result.size(); i++) cout << result[i] << ",";
    cout << endl;
    vector<int> source;
    invertPerm(source, result);
    for(int i = 0; i < source.size(); i++) cout << source[i] << ",";
    cout << endl;

    cout << "============================" << endl;
    int m = 50;
    vector<int> data;
    for(int i = 0; i < n; i++) data.emplace_back((rand() %50)+1);
    for(int i = 0; i < data.size(); i++) cout << data[i] << ",";
    cout << endl;
    int count = reorderbyPerm(data, result);
    cout << "reorder:" << count << endl;
    for(int i = 0; i < data.size(); i++) cout << data[i] << ",";
    cout << endl;

    return 0;
}
