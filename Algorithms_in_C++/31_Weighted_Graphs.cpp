

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

class mycomp
{
public: 
    bool operator()(const we* a, const we* b) 
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
    
    priority_queue<we*, vector<we*>, mycomp> pq;
    map<int, we> wemap;
    vector<bool> seen(n, false);
    int next = 0;
    seen[next] = true;

    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < wes[next].size(); j++)
	{
	    we w = wes[next][j];
	    
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
	cout << pe->s << "," << pe->e << "," << pe->w << "," << pe->i << endl;
	seen[next] = true;
        tree[pe->i] = true;	
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
   
#if 1 
    int sum = 0;
    int r = findMinTree(sample,weight, ELEMOF(sample), n, tree);
    for(int i = 0; i < tree.size(); i++)
    { 
	if (tree[i] == false) continue;
	cout << sample[i] << ',';
	sum += weight[i];
    }
    cout << endl;   
    cout << "result is " << r << "," << sum << endl;

#else    
    priority_queue<we*, vector<we*>, mycomp> pq;
    we w1 = {3,2,1}; pq.push(&w1);
    we w2 = {1,2,3}; pq.push(&w2);
    we w3 = {0,0,0}; pq.push(&w3);
    we* w = pq.top(); pq.pop();
    cout << w->w;
    w = pq.top(); pq.pop();
    cout << w->w;
    w = pq.top(); pq.pop();
    cout << w->w;
#endif

    return 0;
}
