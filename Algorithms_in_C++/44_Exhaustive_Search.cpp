
// incomplete
// 1. Exhausive search in graphs (TODO:backtracking, branch and bound)
// 2. digression: permutation generation 
// 3. approximation algorithm (TODO: simple euclidean travelling salesman tour)

#include <iostream>
#include <vector>
#include <time.h>
#include <stdio.h>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

void getLink(const char* sample[], int num, int n, vector<vector<int>> &links)
{
    links.resize(n);	
    for(int i = 0; i < num; i++)
    {
        int s = sample[i][0] - 'A';
	int e = sample[i][1] - 'A';
        links[s].emplace_back(e);
	links[e].emplace_back(s);
    }
}

void recordCycle(vector<vector<int>> &links, vector<vector<int>> &result, vector<int> &mark)
{
    int n = links.size();	
    
    vector<int> order(n);
    for(int i = 0; i < n; i++) order[mark[i]] = i;
    int s = order[0];
    int e = order[n-1];
    bool found = false; 
    for(int i = 0; i < links[s].size(); i++)
        if (e == links[s][i]) { found = true; break; }	
    if (found) result.emplace_back(order);	
}

void visitCycle(vector<vector<int>> &links, vector<vector<int>> &result, vector<int> &mark, int start, int id)
{
    mark[start] = id;	
    if ((id+1) == links.size()) recordCycle(links, result, mark);

    for(int i = 0; i < links[start].size(); i++)
    {
	int next = links[start][i];    
        if (mark[next] != -1) continue;
	visitCycle(links, result, mark, next, id+1);
    }

    mark[start] = -1;
}

bool checkConnect(vector<vector<int>> &links, vector<int> mark)
{
    int s = -1;	
    int si;
    for(int i = 0; i < links.size(); i++)
        if (s < mark[i]) { s = mark[i]; si = i; }

    // strange things and bypass this check 
    if (s == -1) { cout << "no mark" << endl; return true; }
    for(int i = s+1; i < links.size(); i++)
    {
	bool found;   
        if (links[si].size() == 0) { cout << "wrong links" << endl; return true; }
        for(int j = 0; j < links[si].size(); j++) 
	{
            int next = links[si][j];
	    if (mark[next] != -1) continue;
	    si = next; mark[next] = i; found = true; break;
	}

	if (found == false) return false;
    }

    return true;
}

void visitCycle2(vector<vector<int>> &links, vector<vector<int>> &result, vector<int> &mark, int check, int start, int id)
{
    mark[start] = id;
    if ((id+1) == check && !checkConnect(links, mark)) { mark[start] = -1; return; }
    if ((id+1) == links.size()) recordCycle(links, result, mark);

    for(int i = 0; i < links[start].size(); i++)
    {
	int next = links[start][i];    
        if (mark[next] != -1) continue;
	visitCycle2(links, result, mark, check, next, id+1);
    }

    mark[start] = -1;
}

void getCycle(vector<vector<int>> &links, vector<vector<int>> &result, int method = 0)
{
    vector<int> mark(links.size(), -1);
    if (method == 0) visitCycle(links, result, mark, 0, 0);
    if (method == 1) visitCycle2(links, result, mark, 3, 0, 0);
}

void getPermutation(int k, int n, vector<vector<int>> &result)
{
    if (n > k) return;
    if (n == 1)
    {
        result.resize(k);
	for(int i = 0; i < k ; i++) result[i].emplace_back(i+1);
	return;
    }

    if (k == 1) 
    {
        result.resize(1);
	result[0].emplace_back(k);
	return;
    }

    getPermutation(k-1, n-1, result);
    vector<vector<int>> base = result;
    result.clear();
    getPermutation(k-1, n, result);
    for(int i = 0; i < base.size(); i++)
    {
        for(int j = 0; j < n; j++)
	{
            result.emplace_back(base[i]);
	    vector<int> &v = result[result.size()-1];
	    auto it = v.begin();
	    it += j;
	    v.emplace(it, k);
	}
    }
}

void getPermutation2(int k, vector<vector<int>> &result)
{
    int n = k;
    int kk = k-n+1;
    result.resize(kk);
    for(int i = 0; i < kk ; i++) result[i].emplace_back(i+1);
    
    for(int m = 2; m <= n; m++, kk++)
    {
	vector<vector<int>> base = result;
        result.clear();	
        for(int i = 0; i < base.size(); i++)
        {
            for(int j = 0; j < m; j++)
	    {
                result.emplace_back(base[i]);
	        vector<int> &v = result[result.size()-1];
	        auto it = v.begin();
	        it += j;
	        v.emplace(it, kk+1);
	    }
        }
    }
}

void getCombination(int k, int n, vector<vector<int>> &result)
{
    if (n > k) return;
    if (n == 1)
    {
        result.resize(k);
	for(int i = 0; i < k ; i++) result[i].emplace_back(i+1);
	return;
    }

    if (k == 1) 
    {
        result.resize(1);
	result[0].emplace_back(k);
	return;
    }

    getCombination(k-1, n-1, result);
    vector<vector<int>> base = result;
    result.clear();
    getCombination(k-1, n, result);
    for(int i = 0; i < base.size(); i++)
    {
        result.emplace_back(base[i]);
	vector<int> &v = result[result.size()-1];
	v.emplace(v.end(), k);
    }
}

int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","BC","AF","BD","CE","FD","FE","GE",
	                    "EL","GH","HI","IK","KJ","JL","JM","LM"};
    
    int n = 'M'-'A'+1;
    vector<vector<int>> links;
    getLink(sample, ELEMOF(sample), n, links);
    vector<vector<int>> result;
    time_t t1,t2;
    t1 = time(NULL);
    for(int i = 0; i < 100000; i++) { result.clear(); getCycle(links, result); }
    t2 = time(NULL);
    printf("%f\n",difftime(t2, t1));
    for(int i = 0; i < result.size(); i++)
    {
        for(int j = 0; j < result[i].size(); j++) cout << result[i][j] << ",";
	cout << endl;
    }
    
    cout << "===============================" << endl;
    vector<vector<int>> perm;
    getPermutation(4, 2, perm);
    for(int i = 0; i < perm.size(); i++)
    {
        for(int j = 0; j < perm[i].size(); j++) cout << perm[i][j] << ",";
	cout << endl;
    }

    cout << "===============================" << endl;
    vector<vector<int>> perm2;
    getPermutation2(4, perm2);
    for(int i = 0; i < perm2.size(); i++)
    {
        for(int j = 0; j < perm2[i].size(); j++) cout << perm2[i][j] << ",";
	cout << endl;
    }
    
    cout << "===============================" << endl;
    vector<vector<int>> comb;
    getCombination(4, 3, comb);
    for(int i = 0; i < comb.size(); i++)
    {
        for(int j = 0; j < comb[i].size(); j++) cout << comb[i][j] << ",";
	cout << endl;
    }
    
    return 0;
}
