
#include <iostream>
#include <vector>
#include <deque>
#include <set>

// transitive Closure
//
//

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))
typedef struct _edge 
{
    int s;
    int e;
    int w;
}edge;

void findClosure(const char* sample[], int num, int n, int start, set<int>* ps = NULL)
{
    vector<vector<edge>> edges(n);

    for (int i = 0; i < num; i++)
    {
	int s = sample[i][0] - 'A';
	int e = sample[i][1] - 'A';

	edge ee = {s, e};
        edges[s].emplace_back(ee);
    }

    set<int> result;
    deque<int> stack;
    stack.push_front(start);
    result.insert(start);

    while(stack.size() > 0)
    {
	int s = stack.front(); stack.pop_front();
        for(int i = 0; i < edges[s].size(); i++)
	{
	    int e = edges[s][i].e;
	    if (result.find(e) != result.end())
                continue;
	    stack.push_front(e);
	    result.insert(e);
	}
    }

    cout << (char)('A'+start) << ":";
    for (auto it = result.begin(); it != result.end(); it++)
	 cout << (char)('A'+*it) << ",";
    cout << endl;

    if (ps != NULL) *ps = result;
}

void strongConnected(vector<set<int>> &reach, int n)
{
    vector<int> group(n, 0);
    int id = 0;

    for(int i = 0; i < n; i++)
    {
        if (group[i] != 0) continue;
	group[i] = ++id;
	for(auto it = reach[i].begin(); it != reach[i].end(); it++)
            if (reach[*it].find(i) != reach[*it].end())
		group[*it] = id;    
    }

    for(int i = 0; i < n; i++)
        cout << (char)('A'+i) << "=" << group[i] << endl;   
}

void extendMatrix(vector<vector<int>> &edges, const char* sample[], int num, int n, const int* weight = NULL)
{
    for (int i = 0; i < n; i++) edges[i].resize(n);
    //if (weight == NULL) for (int i = 0; i < n; i++) edges[i][i] = 1;
    for (int i = 0; i < num; i++)
    {
	int s = sample[i][0] - 'A';
	int e = sample[i][1] - 'A';

        edges[s][e] = (weight == NULL) ? 1 : weight[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << edges[i][j] << ',';
        cout << endl;
    }
}

void findClosureAll(vector<vector<int>> &edges, const char* sample[], int num, int n)
{
    extendMatrix(edges, sample, num, n);

    for(int y = 0; y < n; y++)
	for (int x = 0; x < n; x++)
            if (edges[x][y])
                for (int j = 0; j < n; j++)
		    if (edges[y][j]) edges[x][j] = 1;	

    cout << "================" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << edges[i][j] << ',';
        cout << endl;
    }
}

void findShortest(vector<vector<int>> &edges, const char* sample[], const int* weight, int num, int n)
{
    extendMatrix(edges, sample, num, n, weight);

    for(int y = 0; y < n; y++)
	for (int x = 0; x < n; x++)
            if (edges[x][y])
                for (int j = 0; j < n; j++)
		{		
		    if (edges[y][j] == 0) continue; 
		    if (edges[x][j] == 0 || edges[x][j] > (edges[x][y]+edges[y][j])) 
			edges[x][j] = edges[x][y]+edges[y][j];	
                }

    cout << "================" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << edges[i][j] << ',';
        cout << endl;
    }
}

void strongConnected2(vector<vector<int>> &edges, int n)
{
    vector<int> group(n, 0);
    int id = 0;

    for(int i = 0; i < n; i++)
    {
        if (group[i] != 0) continue;
	group[i] = ++id;
	for(int j = 0; j < n; j++)
	    if (edges[i][j] && edges[j][i])	
		group[j] = id;    
    }

    for(int i = 0; i < n; i++)
        cout << (char)('A'+i) << "=" << group[i] << endl;   
}

int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","CA","LM","JM","JL","JK","ED","DF",
	                    "HI","FE","AF","GE","GC","HG","GJ","LG","IH","ML"};
    const int weight[] = {4,1,1,1,2,3,1,2,1, 1,2,2,1,1,3,1,5,1,1};
  
    char start = 'A';
    char end = 'M';
    int num = end-start+1;
    vector<set<int>> fcs(num);
    for (char t = start; t <= end; t++)
        findClosure(sample, ELEMOF(sample), num, t-start, &fcs[t-start]);
    strongConnected(fcs, num);  
    
    vector<vector<int>> edges(num);
    findClosureAll(edges, sample, ELEMOF(sample), num);
    for (int i = 0; i< num; i++) edges[i].clear();
    findShortest(edges, sample, weight, ELEMOF(sample), num);
    strongConnected2(edges, num);

    return 0;
}

