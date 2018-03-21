

#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))
typedef struct weight_edge
{
    int s;
    int e;
}we;

bool isCycle(vector<we*> &now, we* pe, vector<int> &dad, bool update = false)
{
    int s = pe->s;
    int e = pe->e;

    while(dad[s] != -1) s = dad[s];
    while(dad[e] != -1) e = dad[e];
    if (update && s < e) dad[e] = s;
    if (update && e < s) dad[s] = e;

    return (s == e);
}

int getNeighbor(const char* sample[], int num, vector<vector<we>> & wes)
{
    for(int i = 0; i< num; i++)
    {
        int s = sample[i][0]-'A';
        int e = sample[i][1]-'A';
        we w1 = { s, e };	
	we w2 = { e, s };

	wes[s].emplace_back(w1);
	wes[e].emplace_back(w2);
    }
}

void visitDFS(int start, vector<vector<we>> &wes, vector<int> &seq, vector<bool> &mask)
{
    seq.emplace_back(start);
    mask[start] = true;
    for(int i = 0; i < wes[start].size(); i++)
    {
	we &w = wes[start][i];
	if (mask[w.e]) continue;
	visitDFS(w.e, wes, seq, mask);
    }
}

void visitDFS2(int start, vector<vector<we>> &wes, vector<int> &seq)
{
    deque<int> stack;
    set<int> mask;
    stack.push_front(start);

    while(stack.size() > 0)
    {
        start = stack.front(); stack.pop_front();
        if (mask.find(start) != mask.end()) continue;	
        seq.emplace_back(start);
        mask.insert(start);

        for(int i = wes[start].size()-1; i >=0 ; i--)
        {
	    we &w = wes[start][i];
            stack.push_front(w.e);	    
        }
    }

}

bool checkRoot(int start, vector<vector<we>> &wes)
{
    int min = (start == 0) ? 1: 0;
    vector<int> dad(wes.size(), -1);
    for(int i = 0; i < wes.size(); i++)
    {
	if (i == start) continue;
	for(int j = 0; j < wes[i].size(); j++)
	{
            we &w = wes[i][j];
	    if (w.e == start) continue;
	    int s = w.s; while(dad[s] != -1) s = dad[s];
	    int e = w.e; while(dad[e] != -1) e = dad[e];
	    if (s > e) dad[s] = e;
	    if (e > s) dad[e] = s;
	}
    }

    for(int i = 0; i< wes.size(); i++)
    {
        if (i == start) continue;
	int j = i;
	while(dad[j] != -1) j = dad[j];
	//cout << i << " " << j << " " << dad[i] << endl;
	if (j != min) return false;
    }

    return true;
}

int visitPoint(int start, vector<vector<we>> &wes, vector<int> &seq, vector<int> &depth, set<int> &result, int d = 0)
{
    seq.emplace_back(start);
#if 1 
    depth[start] = seq.size();
    int min = seq.size();
#else    
    depth[start] = d;
    int min = d;
#endif

    for(int i = 0; i < wes[start].size(); i++)
    {
	we &w = wes[start][i];
	if (depth[w.e] != -1) 
	{
	    if (depth[w.e] < min) min = depth[w.e];
	}else
        {
	    int m = visitPoint(w.e, wes, seq, depth, result, d+1);
    	    if (m < min) min = m;
	    if (m >= depth[start]) 
	    {
		if (d != 0 || checkRoot(start, wes) == false) 
		    result.insert(start);
	    }
	}
    }

    //cout << start << ":" << d << ":" << min << endl;
    return min;
}

void visitBFS2(int start, vector<vector<we>> &wes, vector<int> &seq, vector<bool> &mask)
{
    deque<int> queue;
    queue.push_back(start);

    while(queue.size() > 0)
    {
        start = queue.front(); queue.pop_front();
        if (mask[start]) continue;	
        seq.emplace_back(start);
        mask[start] = true;

        for(int i = wes[start].size()-1; i >=0 ; i--)
        {
	    we &w = wes[start][i];
            queue.push_back(w.e);	    
        }
    }

}

int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","AC","AF","CG","DE","FD","FE","GE",
	                    "GL","GJ","GH","HI","KJ","JL","JM","LM"};
  
    char start = 'A';
    char end = 'M';
    int n = end-start+1;
 
    vector<vector<we>> wes(n);
    getNeighbor(sample, ELEMOF(sample), wes);
    
    vector<int> seq;
    vector<bool> mask(n, false);
    visitDFS(start-'A', wes, seq, mask);
    for(int i = 0; i< seq.size(); i++) cout << seq[i] << ",";
    cout << endl;
    
    vector<int> seq2;
    visitDFS2(start-'A', wes, seq2);
    for(int i = 0; i< seq.size(); i++) cout << seq2[i] << ",";
    cout << endl;

    for(char c = start; c <= end; c++)
    {
        vector<int> seq3;
        vector<int> depth(n, -1);
        set<int> result;
        visitPoint(c-'A', wes, seq3, depth, result);
        cout << c << ":";
        for(auto it = result.begin(); it != result.end(); it++) cout << *it << ",";
        cout << endl;
    }

    vector<int> seq4;
    vector<bool> mask4(n, false);
    visitBFS2(start-'A', wes, seq4, mask4);
    for(int i = 0; i< seq.size(); i++) cout << seq4[i] << ",";
    cout << endl;

    return 0;
}
