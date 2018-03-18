
//Chapter 33. Ford-Fulkerson method

#include <iostream>
#include <vector>
#include <deque>

typedef struct weight_edge {
    int s;
    int e;
    int c;
    int f;
}we;

#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))
using namespace std;

void searchPath(vector<vector<we>> &wes, vector<we*> &find, int start, int end)
{
    deque<vector<we*>> dd;
    vector<we*> v; 
    for (int i = 0; i< wes[start].size(); i++)
    {
	we* pwe = &wes[start][i];
	if (pwe->c <= pwe->f) continue;
	vector<we*> v;
	v.emplace_back(pwe);
        dd.push_back(v);
    }

    bool found = false;
    while(!found and dd.size() > 0)
    {
        vector<we*> v = dd.front(); dd.pop_front();
	
	int vs = v[v.size()-1]->e;
        for (int i = 0; i < wes[vs].size(); i++)	
            if (wes[vs][i].c > wes[vs][i].f)
	    {
                vector<we*> vv;
		vv.assign(v.begin(), v.end());
		vv.emplace_back(&wes[vs][i]);
		if (wes[vs][i].e == end)
		{
                    find.assign(vv.begin(), vv.end());
		    found = true;
		    break;
		}
		else
		    dd.push_front(vv);
	    }
    }

    int min = 0;
    for (int i = 0; i <find.size(); i++)
    {	    
        int t = find[i]->c - find[i]->f;
        if (min == 0 || min > t) min = t;
	cout << find[i]->s << "," << find[i]->e << ":";
    }
    cout << min << endl;

    for (int i = 0; i <find.size(); i++)
        find[i]->f += min;
}

void findMaxFlow(int (*sample)[3], int num, int start, int end)
{
    vector<vector<we>> wes(end+1);
    vector<we*> find; 

    for(int i = 0; i < num; i++)
    {
        we w;
	w.s = sample[i][0];
	w.e = sample[i][1];
	w.c = sample[i][2];
	w.f = 0;
	wes[w.s].emplace_back(w);
    }

    while(true)
    {
        find.clear();
        searchPath(wes, find, start, end);
	if (find.size() == 0) break;
    }

    int ssum = 0;
    int esum = 0;
    for(int i = 0; i < wes[start].size(); i++)
        ssum += wes[start][i].f;
    for(int i = start; i < end; i++)
	for(int j = 0; j< wes[i].size(); j++) 
	    if (wes[i][j].e == end)	
                esum += wes[i][j].f;

    cout << ssum << "," << esum << endl;
}

int main(int argc, char* argv[])
{
    int start1 = 1;
    int end1 = 6;
    int sample1[][3] = {{1,2,6},{1,3,8},{2,4,6},{3,5,3},{4,6,8},{5,6,6},{2,5,3},{3,4,3}};
    
    findMaxFlow(sample1, ELEMOF(sample1), start1, end1);
    
    int start2 = 0;
    int end2 = 13;
    int sample2[][3] = {{0,1,1},{0,2,1},{0,3,1},{0,4,1},{0,5,1},{0,6,1},
	                {1,7,1},{1,8,1},{1,9,1},{2,7,1},{2,8,1},{2,12,1},
	                {3,9,1},{3,10,1},{3,11,1},{4,7,1},{4,8,1},
                        {5,10,1},{5,11,1},{5,12,1},{6,9,1},{6,11,1},{6,12,1},
                        {7,13,1},{8,13,1},{9,13,1},{10,13,1},{11,13,1},{12,13,1}};
    
    findMaxFlow(sample2, ELEMOF(sample2), start2, end2);
    return 0;
}
