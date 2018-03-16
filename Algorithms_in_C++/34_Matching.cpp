
#include <iostream>
#include <vector> 
#include <deque>

//find stable matching
//mP =  [ '25134', '12345', '23541', '13245', '53214' ] 
//wP =  [ 'EADBC', 'DEBAC', 'ADBCE', 'CBDAE', 'DBCEA' ]

using namespace std;
typedef vector<int> vint;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

void printPairs(int* pairs, int n)
{
    for(int i=1; i< n; i++)
        cout << "bride " << i << " with groom " << pairs[i] << endl;

}

int main(int argc, char* argv[])
{
    vector<vint> manPrefer, wRank;
    deque<int> dc;
    int man[][5] = {{2,5,1,3,4},{1,2,3,4,5},{2,3,5,4,1},{1,3,2,4,5},{5,3,2,1,4}};
    int woman[][5] = {{5,1,4,2,3},{4,5,2,1,3},{1,4,2,3,5},{3,2,4,1,5},{4,2,3,5,1}};
    int groom[1+ELEMOF(woman)] = { 0 };
    int next[1+ELEMOF(man)] = { 0 };

    for (int i=0; i <= ELEMOF(man); i++)
    {
        vint v;
	if (i != 0) v.assign(man[i-1],man[i-1]+5);
	if (i != 0) dc.push_back(i);
	manPrefer.emplace(manPrefer.end(), v);
    }

    for (int i=0; i <= ELEMOF(woman); i++)
    {
        int d[6] = {0};
	vint v;
	v.assign(d, d+6);
	if (i != 0) for (int j=0; j < 5; j++) v[woman[i-1][j]] = j;
	wRank.emplace(wRank.end(), v);	
    }
   
    while(dc.size() > 0)
    {
        int k = dc.front(); dc.pop_front();
	if (next[k] >= manPrefer[k].size()) break;
        int q = manPrefer[k][next[k]]; next[k]++;
        if (groom[q] == 0 or wRank[q][groom[q]] > wRank[q][k])
	{
	    if (groom[q] != 0) dc.push_front(groom[q]);
	    cout << k << ","<< q << endl;
            groom[q] = k;
	}else
	{
            dc.push_front(k);
	}
    }

    cout << "result is" << endl;
    printPairs(groom, 1+ELEMOF(woman));
    return 0;
}
  

