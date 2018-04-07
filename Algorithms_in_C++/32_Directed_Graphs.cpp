
//complete
//1. texture closure 
//2. all shortest paths 
//3. topological sorting  
//4. strongly connected components

#include <iostream>
#include <vector>
#include <deque>
#include <set>

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

void extendMatrix(vector<vector<int>> &edges, const char* sample[], int num, int n, const int* weight = NULL,bool one = true)
{
    for (int i = 0; i < n; i++) edges[i].resize(n);
    //if (weight == NULL) for (int i = 0; i < n; i++) edges[i][i] = 1;
    for (int i = 0; i < num; i++)
    {
	int s = sample[i][0] - 'A';
	int e = sample[i][1] - 'A';

        edges[s][e] = (weight == NULL) ? 1 : weight[i];
	if (one == false)
            edges[e][s] = (weight == NULL) ? 1 : weight[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << edges[i][j] << ',';
        cout << endl;
    }
}

void findClosureAll(vector<vector<int>> &edges, const char* sample[], int num, int n, bool one = true)
{
    extendMatrix(edges, sample, num, n, NULL, one);

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

void findShortest(vector<vector<int>> &edges, const char* sample[], const int* weight, int num, int n, bool one = true)
{
    extendMatrix(edges, sample, num, n, weight, one);

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

void visit(vector<set<int>> &fcs, vector<bool> &seen, deque<int> &order, int k)
{
    if (seen[k] == true) return;
    else seen[k] = true;	

    for (auto it = fcs[k].begin(); it != fcs[k].end(); it++)
	 if (seen[*it] == false) visit(fcs, seen, order, *it);
    
    order.push_front(k);
}

bool check_topological_sort(const char* sample[], int num, vector<int> result)
{
    vector<int> rank(result.size());
    for(int i = 0; i < result.size(); i++) 
        rank[result[i]] = i;

    for(int i = 0; i < num; i++)
    {
        int s = sample[i][0] - 'A';
        int e = sample[i][1] - 'A';
        if (rank[s] > rank[e]) return false;
    }

    return true;
}

bool merge(vector<int>& result, const vector<deque<int>> &orders)
{
    bool r = true;

    if (orders.size() < 2)
    {	    
        if (orders.size() == 0)	    
            result.assign(orders[0].begin(), orders[0].end());
        return r;
    }

    vector<int> count(result.size(), 0);
    for(int i=0; i < orders.size(); i++)    	
	for(int j=0; j < orders[i].size(); j++)
	{
	    int c = orders[i][j];	
            count[c] ++;        
        }

    //for(int i = 0; i < count.size(); i++) 
    //	cout << count[i] << ",";
    //cout << endl;
    
    vector<int> index(orders.size(), 0);
    int record = 0;
    int next = 0;
    unsigned int acc = 0;
    unsigned int full = (1 <<orders.size())-1;
    while(record < result.size())
    {
        int min = -1;
	int i = index[next];
	if (i < orders[next].size()) 
	{
	    int c = orders[next][i];
            if (count[c] < 2) 
	    { result[record++] = c; index[next]++; }
	    else 
	    { acc |= (1<<next); if (min == -1 || index[min] >index[next]) min = next; }
	}


	if (acc == full)
	{
	    int c = orders[min][index[min]];
	    result[record++] = c;
	    int k = 0;
            for(int j = 0; j < orders.size(); j++)
	    {
		if (orders[j][index[j]] == c) { index[j]++; k++; }
	    }

            if (k != count[c]) r = false;
	    acc = 0;
	}
#if 0
        cout << acc << ":" << next << ":";	
        for(int i = 0; i < index.size(); i++) 
	    cout << index[i] << ",";
        cout << ":";
        for(int i = 0; i < record; i++) 
	    cout << (char)(result[i]+'A');
        cout << endl;
#endif	
  	next = (next+1) % orders.size();
    }
   
    cout << "answer is ";
    for(int i = 0; i < result.size(); i++) 
	cout << (char)(result[i]+'A');
    cout << endl;

    return r;
}

void topological_sort()
{
    const char* sample[] = {"AG","AB","AC","LM","JM","JL","JK","ED","FD",
	                    "HI","FE","AF","GE","GC","GH","JG","LG"};
    char start = 'A';
    char end = 'M';
    int n = end-start+1;
    vector<set<int>> fcs(n);
    for (char t = start; t <= end; t++)
        findClosure(sample, ELEMOF(sample), n, t-start, &fcs[t-start]);
   
    vector<bool> in(n, false);
    vector<bool> out(n, false);
    vector<int> starts;
    for(int i = 0; i < ELEMOF(sample); i++)
    {
        int s = sample[i][0] - 'A';
        int e = sample[i][1] - 'A';
        out[s] = in[e] = true;          
    }

    for(int i = 0; i < n; i++)
    {
	if (out[i] == true and in[i] == false)
	    starts.emplace_back(i);	
    }

    vector<deque<int>> orders(starts.size());
    for(int i = 0; i < starts.size(); i++)
    {
        vector<bool> seen(n, false);
        visit(fcs, seen, orders[i], starts[i]); 
	for(int j = 0; j < orders[i].size(); j++)
	    cout << (char)('A'+orders[i][j]);	
	cout << endl;
    }

    vector<int> result(n);
    bool r = merge(result, orders); 

    bool check = check_topological_sort(sample, ELEMOF(sample), result);
    cout << "check result = " << check << " and " << r << endl;
}

int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","CA","LM","JM","JL","JK","ED","DF",
	                    "HI","FE","AF","GE","GC","HG","GJ","LG","IH","ML"};
    const int weight[] = {4,1,1,1,2,3,1,2,1, 1,2,2,1,1,3,1,5,1,1};
  
    char start = 'A';
    char end = 'M';
    int n = end-start+1;

    vector<set<int>> fcs(n);
    for (char t = start; t <= end; t++)
        findClosure(sample, ELEMOF(sample), n, t-start, &fcs[t-start]);
    strongConnected(fcs, n);  
    
    vector<vector<int>> edges(n);
    findClosureAll(edges, sample, ELEMOF(sample), n);
    for (int i = 0; i< n; i++) edges[i].clear();
    findShortest(edges, sample, weight, ELEMOF(sample), n);
    strongConnected2(edges, n);

    topological_sort();

    const char* sample1[] = {"AG","AB","BC","AF","BD","BE","CE","DE","FD","FE","GE",
	                    "FL","EL","GL","GJ","GH","HI","IK","KJ","JL","JM","LM"};
    const int weight1[] = {6,1,1,2,2,4,4,2,1,2,1, 2,4,5,1,3,2,1,1,3,2,1};
    
    vector<vector<int>> edges2(n);
    findShortest(edges2, sample1, weight1, ELEMOF(sample1), n, false);
    
    return 0;
}

