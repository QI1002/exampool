
#include <iostream>
#include <vector> 
#include <deque>

//find stable matching
//mP =  [ '25134', '12345', '23541', '13245', '53214' ] 
//wP =  [ 'EADBC', 'DEBAC', 'ADBCE', 'CBDAE', 'DBCEA' ]

using namespace std;
typedef vector<int> vint;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))
#define MANS 5
#define WOMANS 5 

void printPairs(int* pairs, int n, bool r = false)
{
    for(int i=1; i< n; i++)
        if (r)    
	    cout << "groom " << i << " with bride " << pairs[i] << endl;
        else 
	    cout << "bride " << i << " with groom " << pairs[i] << endl;
}

int* findMatch(int man[][WOMANS], int woman[][MANS], int ms, int ws)
{
    vector<vint> manPrefer(1+ms); // i1: 1~ms, i2: 0~ws-1
    vector<vint> womanRank(1+ws); // i2: 1~ws, i2: 1~ms
    deque<int> dc;
    int* groom = new int[1+ws];
    int* next = new int[1+ms];

    for (int i=1; i <= ms; i++)
    {
        vint &v = manPrefer[i];
	v.resize(ws);
	for (int j=0; j < ws; j++) v[j] = man[i-1][j];
	dc.push_back(i);
	next[i] = 0;
    }

    for (int i=1; i <= ws; i++)
    {
	vint &v = womanRank[i];
        v.resize(1+ms);	
        for (int j=0; j < ms; j++) v[woman[i-1][j]] = j;
        groom[i] = 0;
    }
  
    while(dc.size() > 0)
    {
        int k = dc.front(); dc.pop_front();
	if (next[k] >= manPrefer[k].size()) break;
        int q = manPrefer[k][next[k]]; next[k]++;
        if (groom[q] == 0 or womanRank[q][groom[q]] > womanRank[q][k])
	{
	    if (groom[q] != 0) dc.push_front(groom[q]);
	    cout << k << ","<< q << endl;
            groom[q] = k;
	}else
	{
            dc.push_front(k);
	}
    }

    delete[] next;
    return groom;
}

bool isStable(int man[][WOMANS], int woman[][MANS], int ms, int ws, int* groom)
{
    int ps = (ms > ws) ? ms+1 : ws+1;
    vector<vint> manRank(1+ms);
    vector<vint> womanRank(1+ws);

    for (int i=1; i <= ms; i++)
    {
	vint &v = manRank[i];
	v.resize(1+ws);
	for (int j=0; j < ws; j++) v[man[i-1][j]] = j;
    }

    for (int i=1; i <= ws; i++)
    {
	vint &v = womanRank[i];
	v.resize(1+ms);
	for (int j=0; j < ms; j++) v[woman[i-1][j]] = j;
    }
    
    for(int i = 1; i < ps; i++)
        for (int j =i+1; j < ps; j++)
	{
            int w1 = i;
	    int w2 = j;
	    int m1 = groom[i];
	    int m2 = groom[j];

	    if (manRank[m1][w2] < manRank[m1][w1] && 
	        womanRank[w2][m1] < womanRank[w2][m2])
	    {
		cout << "m1 " << m1 << "," << w1 << "," << m2 << "," << w2 << endl;    
	        return false;
	    }
	    if (manRank[m2][w1] < manRank[m2][w2] && 
	        womanRank[w1][m2] < womanRank[w1][m1])
	    {
		cout << "m2 " << m1 << "," << w1 << "," << m2 << "," << w2 << endl;    
	        return false;
	    }
	}
 
    return true;
}

int main(int argc, char* argv[])
{
    int man[][MANS] = {{2,5,1,3,4},{1,2,3,4,5},{2,3,5,4,1},{1,3,2,4,5},{5,3,2,1,4}};
    int woman[][WOMANS] = {{5,1,4,2,3},{4,5,2,1,3},{1,4,2,3,5},{3,2,4,1,5},{4,2,3,5,1}};
    int* groom;
    bool check;
    
    groom = findMatch(man, woman, MANS, WOMANS);
    check = isStable(man, woman, MANS, WOMANS, groom);
    cout << "result is with check = " << check << endl;
    printPairs(groom, 1+WOMANS);
    delete[] groom;

    groom = findMatch(woman, man, WOMANS, MANS);
    check = isStable(woman, man, WOMANS, MANS, groom);
    cout << "result is with check = " << check << endl;
    printPairs(groom, 1+MANS, true);
    delete[] groom;
        
    return 0;
}	

