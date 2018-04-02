
#include <iostream>
#include <vector>

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

void visitCycle(vector<vector<int>> &links, vector<vector<int>> &result, vector<int> &mark, int start, int id)
{
    int n = links.size();	
    mark[start] = id;	
    if ((id+1) == n) 
    {
        vector<int> order(n);
	for(int i = 0; i < n; i++) order[mark[i]] = i;
	int s = order[0];
	int e = order[id];
	bool found = false; 
	for(int i = 0; i < links[s].size(); i++)
	    if (e == links[s][i]) { found = true; break; }	
	if (found) result.emplace_back(order);
    }

    for(int i = 0; i < links[start].size(); i++)
    {
	int next = links[start][i];    
        if (mark[next] != -1) continue;
	visitCycle(links, result, mark, next, id+1);
    }

    mark[start] = -1;
}

void getCycle(vector<vector<int>> &links, vector<vector<int>> &result)
{
    vector<int> mark(links.size(), -1);
    visitCycle(links, result, mark, 0, 0);
}

int main(int argc, char* argv[])
{
    const char* sample[] = {"AG","AB","BC","AF","BD","CE","FD","FE","GE",
	                    "EL","GH","HI","IK","KJ","JL","JM","LM"};
    
    int n = 'M'-'A'+1;
    vector<vector<int>> links;
    getLink(sample, ELEMOF(sample), n, links);
    vector<vector<int>> result;
    getCycle(links, result);
    for(int i = 0; i < result.size(); i++)
    {
        for(int j = 0; j < result[i].size(); j++) cout << result[i][j] << ",";
	cout << endl;
    }
    return 0;
}
