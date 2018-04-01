
#include <iostream>
#include <vector>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

int knapsack(int stuff[][2], int num, int cap, vector<int> &result)
{
    int best_values = 0; 
    int best_i;
    vector<int> values(cap+1, 0);
    vector<int> best(cap+1, -1); 
    
    for(int i = 0; i <= cap; i++)
    {
	for(int j = 0; j < num; j++)
	{
            if (stuff[j][0] > i) continue;
	    int t = values[i-stuff[j][0]]+stuff[j][1];
	    if (values[i] < t) {  best[i] = j; values[i] = t; }
	}

        cout << i << ":" << values[i] << ":" << best[i] << endl;
	if (best_values < values[i]) 
	{  best_values = values[i]; best_i = i; }
    }

    cout << best_values << " with " << best_i << endl;
    int i = best_i;
    while (best[i] != -1)  { result.emplace_back(best[i]); i -= stuff[best[i]][0]; }
    return best_values;
}

int main(int argc, char* argv[])
{
    int stuff[][2] = { {3,4}, {4,5}, {7,10}, {8,11}, {9, 13}};
    vector<int> result;

    int values = knapsack(stuff, ELEMOF(stuff), 17, result);
    cout << "The max values are " << values << ":";
    for(int i = 0; i< result.size(); i++) 
    {
	int j = result[i];    
	cout << j << " with (" << stuff[j][0] << "," << stuff[j][1] << ") ,";
    }

    cout << endl;
    return 0;
}
