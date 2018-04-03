
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

    //cout << best_values << " with " << best_i << endl;
    int i = best_i;
    while (best[i] != -1)  { result.emplace_back(best[i]); i -= stuff[best[i]][0]; }
    return best_values;
}

int minMatrixMutiple(int matrix[][2], int num, vector<int> &result)
{
    int a, b;
    vector<vector<int>> m;
    vector<vector<int>> mi;
    
    for(int i = 0; i < num; i++) 
    { 
	vector<int> mm(num, 0); 
	m.emplace_back(mm); 
	vector<int> mmi(num, -1); 
	mi.emplace_back(mmi); 
    }
    
    for(int i = 1; i < num; i++)
    {
        for(int j = 0; j < (num-i); j++)
	{
            a = j;
	    b = j+i;
	    if (i == 1) 
	    {
	        m[a][b] = matrix[a][0]*matrix[a][1]*matrix[b][1];
	        mi[a][b] = a;
	    }
	    else
	    {
                int t1 = m[a+1][b] + matrix[a][0]*matrix[a][1]*matrix[b][1];
		int t2 = m[a][b-1] + matrix[a][0]*matrix[b][0]*matrix[b][1];

		m[a][b] = (t1 < t2) ? t1 : t2;
		mi[a][b] = (t1 < t2) ? a : b;
	    }

            //cout << a << "," << b << ":" << m[a][b] << endl;
	}
    }

    a = 0; b = num-1;
    int j = mi[a][b];
    while(j != -1) 
    { 
	result.emplace_back(j); 
	if (j != a && j != b) cout << j << " is not " << a << " or " << b << endl;  
	if (j == b) { j = mi[a][b-1]; b--; } else { j = mi[a+1][b]; a++; } 
    } 
    return m[0][num-1];
}

int minSearchTree(int tree[][2], int num, vector<int> &result)
{
    int a, b;
    vector<vector<int>> m;
    vector<vector<int>> mi;
    
    for(int i = 0; i < num; i++) 
    { 
	vector<int> mm(num, 0); 
	m.emplace_back(mm); 
	vector<int> mmi(num, -1); 
	mi.emplace_back(mmi); 
    }
    
    for(int i = 0; i < num; i++)
    {
        for(int j = 0; j < (num-i); j++)
	{
            a = j;
	    b = j+i;
	    if (i == 0) 
	    {
	        m[a][b] = tree[j][1];
	        mi[a][b] = a;
	    }
	    else
	    {
		int kk = 0;
		for(int k = a; k <= b; k++) kk += tree[k][1];
                for(int k = a; k <= b; k++) 
		{
                    int kkk = kk + m[a][k-1] + m[k+1][b];
		    if (mi[a][b] == -1 || m[a][b] > kkk) 
		    {
                        mi[a][b] = k;
			m[a][b] = kkk;
		    }
		}
	    }

            cout << a << "," << b << ":" << m[a][b] << endl;
	}
    }

    a = 0; b = num-1;
    vector<pair<int,int>> range;
    int j = 0;
    result.emplace_back(mi[a][b]);
    range.emplace_back(pair<int, int>(a, b));
    while(j < result.size()) 
    { 
	int k = result[j];
	a = range[j].first; 
	b = range[j].second;
	cout << a << "," << b << ":" << k << endl;
	if (a < (k-1)) { result.emplace_back(mi[a][k-1]); range.emplace_back(pair<int,int>(a, k-1)); }
	if ((k+1) < b) { result.emplace_back(mi[k+1][b]); range.emplace_back(pair<int,int>(k+1, b)); }
	j++;
    }		
    
    return m[0][num-1];
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

    int matrix[][2] = { {4,2}, {2,3}, {3,1}, {1,2}, {2,2}, {2,3} };
    vector<int> result2;
    int mtimes = minMatrixMutiple(matrix, ELEMOF(matrix), result2);
    cout << "The min values are " << mtimes << ":";
    int a = result2[result2.size()-1]; int b = a+1;
    string s = "(" + to_string(a) + "x" + to_string(b) + ")";
    for(int i = result2.size()-2; i >= 0; i--) 
    {
	int k = result2[i];
	if (k > a) s = "(" + s + "x" + to_string(k) + ")";
	else s = "(" + to_string(k) + "x" + s + ")";
    }
    cout << s << endl;

    int stree[][2] = { {'A',4}, {'B',2}, {'C',1}, {'D',3}, {'E',5}, {'F',2}, {'G',1} };
    vector<int>result3;
    int stimes = minSearchTree(stree, ELEMOF(stree), result3);
    cout << "The min values are " << stimes << ":";
    for(int i = 0; i< result3.size(); i++) cout << result3[i] << ","; 
    cout << endl;

    return 0;
}
