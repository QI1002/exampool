

#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))
typedef struct weight_edge
{
    int s;
    int e;
    int w;   
    int i;
}we;

typedef struct weight_path
{
    vector<int> p;
    int n;
    int w;
    bool inheap;
}wp;

class wecomp
{
public: 
    bool operator()(const we* a, const we* b) 
    {
        return a->w > b->w;
    }
};

class wpcomp
{
public: 
    bool operator()(const wp* a, const wp* b) 
    {
        return a->w > b->w;
    }
};

bool findMinTree(const char* sample[], const int weight[], const int num, int n, vector<bool> &tree)
{
    vector<vector<we>> wes(n);	
    for(int i = 0; i < num ; i++)
    {
        we w1,w2;
	w1.s = sample[i][0]-'A';
	w1.e = sample[i][1]-'A';
	w1.w = weight[i];
        w1.i = i;

	w2.s = sample[i][1]-'A';
	w2.e = sample[i][0]-'A';
	w2.w = weight[i];
        w2.i = i;
        	
	wes[w1.s].emplace_back(w1);
	wes[w2.s].emplace_back(w2);
    }
    
    priority_queue<we*, vector<we*>, wecomp> pq;
    map<int, we> wemap;
    vector<bool> seen(n, false);
    int next = 0;
    seen[next] = true;

    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < wes[next].size(); j++)
	{
	    we w = wes[next][j];
	    if (seen[w.e]) continue;
	    
	    if (wemap.find(w.e) != wemap.end())
	    {
		if (w.w < wemap[w.e].w)    
                    wemap[w.e] = w;
	    }
	    else
	    {
	        wemap.insert(pair<int, we>(w.e, w));
	    }

	    pq.push(&wemap[w.e]);
	}

	we* pe = NULL;
	do {
	    if (pq.size() == 0) break;
	    pe = pq.top(); pq.pop();
      	    next = pe->e;
	    //cout << seen[next] << " " << next;
	    //cout << "<<" << pe->s << "," << pe->e << "," << pe->w << "," << pe->i << endl;
	}while(seen[next]);
       
	if (pe == NULL) return false;
	//cout << pe->s << "," << pe->e << "," << pe->w << "," << pe->i << endl;
	seen[next] = true;
        tree[pe->i] = true;	
    }

    return true;
}

bool findShortestPath(const char* sample[], const int weight[], const int num, int n, int start, vector<wp> &path)
{
    vector<vector<we>> wes(n);	
    for(int i = 0; i < num ; i++)
    {
        we w1,w2;
	w1.s = sample[i][0]-'A';
	w1.e = sample[i][1]-'A';
	w1.w = weight[i];
        w1.i = i;

	w2.s = sample[i][1]-'A';
	w2.e = sample[i][0]-'A';
	w2.w = weight[i];
        w2.i = i;
	
	wes[w1.s].emplace_back(w1);
	wes[w2.s].emplace_back(w2);
    }

    priority_queue<wp*, vector<wp*>, wpcomp> pq;
    vector<bool> seen(n, false);
    int next = 0;
    
    for(int i = 1; i < n; i++) 
    { path[i].n = i; path[i].w = -1; path[i].inheap = false; }
    path[next].inheap = seen[next] = true;
    path[next].p.emplace_back(next);
    
    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < wes[next].size(); j++)
	{
	    we w = wes[next][j];
	    if (seen[w.e]) continue;
            int ww = w.w + path[next].w;

	    if (path[w.e].w == -1 || ww < path[w.e].w)    
	    {
                path[w.e].w = ww;
		path[w.e].p = path[next].p;
		path[w.e].p.emplace_back(w.e);
	        if (path[w.e].inheap == false) 
	        {
		    pq.push(&path[w.e]);
		    path[w.e].inheap = true;
	        }
	    }

	}

	wp* wpe = NULL;
	do {
	    if (pq.size() == 0) break;
	    wpe = pq.top(); pq.pop();
      	    next = wpe->n;
	    //cout << seen[next] << " " << next;
	    //cout << "<<" << wpe->n << "," << wpe->w << endl;
	}while(seen[next]);
       
	if (wpe == NULL) return false;
	//cout << wpe->n << "," << wpe->w << endl;
	seen[next] = true;
    }

    return true;
}


int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","BC","AF","BD","BE","CE","DE","FD","FE","GE",
	                    "FL","EL","GL","GJ","GH","HI","IK","KJ","JL","JM","LM"};
    const int weight[] = {6,1,1,2,2,4,4,2,1,2,1, 2,4,5,1,3,2,1,1,3,2,1};
  
    char start = 'A';
    char end = 'M';
    int n = end-start+1;
   
    vector<bool> tree(ELEMOF(sample), false);
    int sum = 0;
    bool r1 = findMinTree(sample, weight, ELEMOF(sample), n, tree);
    for(int i = 0; i < tree.size(); i++)
    { 
	if (tree[i] == false) continue;
	cout << sample[i] << ',';
	sum += weight[i];
    }
    cout << endl;   
    cout << "result is " << r1 << "," << sum << endl;
    
    vector<wp> path(n);
    bool r2 = findShortestPath(sample, weight, ELEMOF(sample), n, start, path);
    for(int i = 0; i < path.size(); i++)
    { 
	cout << i << ":" << path[i].w << ',';
    }
    cout << endl;   
    cout << "result is " << r2 << endl;

    return 0;
}
