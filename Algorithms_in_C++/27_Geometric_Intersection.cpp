
//complete
//1. Horizontal and vertical lines for two directions
//2. The intersection of 1s lines


#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _line1d 
{
    int s,e;
}line1d;

typedef struct _point 
{
    int x,y;
}point;

typedef struct _line 
{
    point s,e;
}line;

typedef struct _hline
{
    int value;	
    int tag; // 1: vertical line 0,2:start/end of horizontal line
    int index;
}hline;

class hcomp
{
public:
    bool operator()(const hline &a, const hline &b)
    {
	if (a.value == b.value) return a.tag < b.tag;    
        return a.value < b.value;
    }
};

void getIntersectByH(const line ls[], int num, vector<pair<int, int>> &result)
{
    vector<hline> hh;	
    for(int i = 0; i< num; i++)
    {
        bool isV = ls[i].s.x == ls[i].e.x;
        bool isH = ls[i].s.y == ls[i].e.y;

        hline h;	
	if (isV) 
	{
	    hline h = { ls[i].s.x, 1, i };
	    hh.emplace_back(h);
	}
	if (isH) 
	{ 
	    hline h1 = { ls[i].s.x, 0, i }; 
	    hline h2 = { ls[i].e.x, 2, i }; 
	    hh.emplace_back(h1);
	    hh.emplace_back(h2);
	}
    }

    sort(hh.begin(), hh.end(), hcomp());
    set<int> inH;
    for(int i = 0; i< hh.size(); i++)
    {
        int j = hh[i].index;
	    
        if (hh[i].tag == 0) inH.insert(j);
        
	if (hh[i].tag == 1)
	{
	    for(auto it = inH.begin(); it != inH.end(); it++)
	    {
		int hi = *it;    
                if (ls[j].s.y <= ls[hi].s.y &&
		    ls[j].e.y >= ls[hi].e.y)
		    result.emplace_back(pair<int,int>(j, hi));	
	    }
	}

        if (hh[i].tag == 2) inH.erase(j);
    }
}

typedef struct _vline
{
    int value;	
    int tag; // 1: horizontal line 0,2:start/end of vertical line
    int index;
}vline;

class vcomp
{
public:
    bool operator()(const vline &a, const vline &b)
    {
	if (a.value == b.value) return a.tag < b.tag;    
        return a.value < b.value;
    }
};

void getIntersectByV(const line ls[], int num, vector<pair<int, int>> &result)
{
    vector<vline> vv;	
    for(int i = 0; i< num; i++)
    {
        bool isV = ls[i].s.x == ls[i].e.x;
        bool isH = ls[i].s.y == ls[i].e.y;

        vline v;	
	if (isH) 
	{
	    vline v = { ls[i].s.y, 1, i };
	    vv.emplace_back(v);
	}
	if (isV) 
	{ 
	    vline v1 = { ls[i].s.y, 0, i }; 
	    vline v2 = { ls[i].e.y, 2, i }; 
	    vv.emplace_back(v1);
	    vv.emplace_back(v2);
	}
    }

    sort(vv.begin(), vv.end(), vcomp());
    set<int> inV;
    for(int i = 0; i< vv.size(); i++)
    {
        int j = vv[i].index;
	    
        if (vv[i].tag == 0) inV.insert(j);
        
	if (vv[i].tag == 1)
	{
	    for(auto it = inV.begin(); it != inV.end(); it++)
	    {
		int vi = *it;    
                if (ls[j].s.x <= ls[vi].s.x &&
		    ls[j].e.x >= ls[vi].e.x)
		    result.emplace_back(pair<int,int>(j, vi));	
	    }
	}

        if (vv[i].tag == 2) inV.erase(j);
    }
}

int CCW(point &p0, point &p1, point &p2)
{
    int dx1, dx2, dy1, dy2;
    
    dx1 = p1.x - p0.x; dy1 = p1.y - p0.y;
    dx2 = p2.x - p0.x; dy2 = p2.y - p0.y;

    if (dx1*dy2 > dy1*dx2) return 1;
    if (dx1*dy2 < dy1*dx2) return -1;
    // if equal means dx1/dy1 == dx2/dy2
    if ((dx1*dx2 <= 0) || (dy1*dy2 <= 0)) return -1;
    if ((dx1*dx1+dy1*dy1) < (dx2*dx2+dy2*dy2)) return 1;
    return 0;
}

bool isIntersect(line l1, line l2)
{
    int ccw1 = CCW(l1.s, l1.e, l2.s);
    int ccw2 = CCW(l1.s, l1.e, l2.e);
    int ccw3 = CCW(l2.s, l2.e, l1.s);
    int ccw4 = CCW(l2.s, l2.e, l1.e);

    //cout << ccw1 << " " << ccw2 << " " << ccw3 << " " << ccw4 << endl;
    return (ccw1*ccw2 <= 0 && ccw3*ccw4 <= 0);
}

void getIntersect(const line ls[], int num, vector<pair<int, int>> &result)
{
    for(int i = 0; i < num; i++)
	for(int j = i+1; j < num; j++)
	{
            if (isIntersect(ls[i], ls[j])) 
		result.emplace_back(pair<int, int>(i, j));
        }
}

typedef struct _hline1d
{
    int value;	
    int tag; // 0,1:start/end of horizontal line
    int index;
}hline1d;

class hcomp1d
{
public:

    bool operator()(const hline1d &a, const hline1d &b)
    {
	if (a.value == b.value) 
	{
            if (a.tag == b.tag)
	    {
                if (a.tag == 0) return a.index < b.index;
		else return a.index > b.index;	
	    }
	    else return a.tag < b.tag;    
	}

        return a.value < b.value;
    }
};

class paircomp
{
public:

    bool operator()(const pair<int,int> &a, const pair<int,int> &b)
    {
	if (a.first == b.first) 
	    return a.second < b.second;    
        return a.first < b.first;
    }
};

bool getOverlay(const line1d &l1, const line1d &l2, line1d &overlay)
{
    if (l1.s <= l2.s && l2.s <= l1.e)
    {
        if (l1.e <= l2.e) 
	{ overlay.s = l2.s; overlay.e = l1.e; return true; }
	else 	
	{ overlay.s = l2.s; overlay.e = l2.e; return true; } 
    }

    if (l2.s <= l1.s && l1.s <= l2.e)
    {
        if (l2.e <= l1.e) 
	{ overlay.s = l1.s; overlay.e = l2.e; return true; }
	else 	
	{ overlay.s = l1.s; overlay.e = l1.e; return true; } 
    }

    return false;
}

void getFastIntersect1d(const vector<line1d> vl1s, vector<pair<int, int>> &result)
{
    vector<hline1d> hh;	
    for(int i = 0; i< vl1s.size(); i++)
    {
        hline1d h1 = { vl1s[i].s, 0, i }; 
        hline1d h2 = { vl1s[i].e, 1, i }; 
        hh.emplace_back(h1);
        hh.emplace_back(h2);
    }

    sort(hh.begin(), hh.end(), hcomp1d());
    set<int> inH;
    for(int i = 0; i< hh.size(); i++)
    {
        int j = hh[i].index;
	    
        if (hh[i].tag == 0) 
	{
	    for(auto it = inH.begin(); it != inH.end(); it++)
	    {
		int hi = *it;    
		if (j <hi) result.emplace_back(pair<int,int>(j, hi));	
		else result.emplace_back(pair<int,int>(hi, j));	
	    }
	    inH.insert(j);
        }

        if (hh[i].tag == 1) inH.erase(j);
    }

    sort(result.begin(), result.end(), paircomp());
}	

void getIntersect1d(const line1d l1s[], int num, vector<pair<int, int>> &result)
{
    for(int i = 0; i< num; i++)
	for(int j = i+1; j< num; j++)    
        {
	    line1d overlay;

	    if (getOverlay(l1s[i], l1s[j], overlay))
		result.emplace_back(pair<int, int>(i, j));    
        }
}	

void getGeneralIntersect(const line ls[], int num, vector<pair<int, int>> &result)
{
    vector<line1d> xlines;
    vector<line1d> ylines;

    for(int i = 0; i< num; i++)
    {
        line1d xl,yl;
	
	if (ls[i].s.x < ls[i].e.x)
	{
	    xl.s = ls[i].s.x;
	    xl.e = ls[i].e.x;
	}else
	{
	    xl.e = ls[i].s.x;
	    xl.s = ls[i].e.x;
	}

	if (ls[i].s.y < ls[i].e.y)
	{	
            yl.s = ls[i].s.y;
	    yl.e = ls[i].e.y;
	}else
	{
	    yl.e = ls[i].s.y;
	    yl.s = ls[i].e.y;
	}

	xlines.emplace_back(xl);
	ylines.emplace_back(yl);
    }

    vector<pair<int, int>> resultx;		  
    getFastIntersect1d(xlines, resultx);         
    //for(int i = 0; i < resultx.size(); i++)
    //	cout << resultx[i].first << " " << resultx[i].second << endl;
    
    vector<pair<int, int>> resulty;		  
    getFastIntersect1d(ylines, resulty);         
    //for(int i = 0; i < resulty.size(); i++)
    //	cout << resulty[i].first << " " << resulty[i].second << endl;

    int x = 0;
    int y = 0;
    paircomp t;
    while(x < resultx.size() && y < resulty.size())
    {
	if (resultx[x] == resulty[y])
	{
            if (isIntersect(ls[resultx[x].first], ls[resultx[x].second]))	    
	        result.emplace_back(resultx[x]);
	    x++; y++; continue;
	}

        bool r = t(resultx[x], resulty[y]);
        if (r) x++; else y++;   
    }
}

int main(int argc, char* argv[])
{
    line ls[] = { {{0,12}, {11,12}}, {{6,9}, {6,11}},{{2,0}, {2,10}},   
                  {{5,4}, {5,20}}, {{9,2}, {9,14}},{{0,9}, {0,22}},   
                  {{7,6}, {15,6}}, {{10,10}, {10,20}}, {{14,7}, {14,12}}};   

    line1d l1s[] = { {12,12}, {9,11}, {0,10}, {4,20}, {2,14}, {9,22}, {6,6}, {10,20}, {7,12}};   

    // DF, FI, HI 
    line ls2[] = { {{2,16}, {1,22}}, {{10,5}, {5,14}},{{3,2}, {5,8}},   
                   {{9,12}, {2,25}}, {{13,20}, {10,22}},{{1,10}, {11,27}},   
                   {{23,7}, {22,19}}, {{14,4}, {15,25}}, {{24,22}, {4,27}}};   
    
    vector<pair<int, int>> resultH;		  
    getIntersectByH(ls, ELEMOF(ls), resultH);         
    for(int i = 0; i < resultH.size(); i++)
	cout << resultH[i].first << " " << resultH[i].second << endl;
    cout << "==============================" << endl; 
    vector<pair<int, int>> resultV;		  
    getIntersectByV(ls, ELEMOF(ls), resultV);         
    for(int i = 0; i < resultV.size(); i++)
	cout << resultV[i].first << " " << resultV[i].second << endl;
    cout << "==============================" << endl; 
    vector<pair<int, int>> result;		  
    getIntersect(ls, ELEMOF(ls), result);         
    for(int i = 0; i < result.size(); i++)
	cout << result[i].first << " " << result[i].second << endl;
    
    cout << "==============================" << endl; 
    vector<pair<int, int>> resultf1d;		  
    vector<line1d> vl1s; vl1s.assign(l1s, l1s+ELEMOF(l1s));
    getFastIntersect1d(vl1s, resultf1d);         
    for(int i = 0; i < resultf1d.size(); i++)
    {
	int j = resultf1d[i].first;
	int k = resultf1d[i].second;
	line1d overlay;
	bool r = getOverlay(l1s[j], l1s[k], overlay);
	cout << j << "(" << l1s[j].s << "," << l1s[j].e << ")&"; 
	cout << k << "(" << l1s[k].s << "," << l1s[k].e << ")=";
	if (r) 	cout << "(" << overlay.s << "," << overlay.e << ")" << endl;
	else cout << "(NULL)" << endl;
    }   
    cout << "==============================" << endl; 
    vector<pair<int, int>> result1d;		  
    getIntersect1d(l1s, ELEMOF(l1s), result1d);         
    for(int i = 0; i < result1d.size(); i++)
    {
	int j = result1d[i].first;
	int k = result1d[i].second;
	line1d overlay;
	bool r = getOverlay(l1s[j], l1s[k], overlay);
	cout << j << "(" << l1s[j].s << "," << l1s[j].e << ")&"; 
	cout << k << "(" << l1s[k].s << "," << l1s[k].e << ")=";
	if (r) 	cout << "(" << overlay.s << "," << overlay.e << ")" << endl;
	else cout << "(NULL)" << endl;
    }   
   
    cout << "==============================" << endl; 
    vector<pair<int, int>> result2;		  
    getIntersect(ls2, ELEMOF(ls2), result2);         
    for(int i = 0; i < result2.size(); i++)
	cout << result2[i].first << " " << result2[i].second << endl;

    cout << "==============================" << endl; 
    vector<pair<int, int>> resultg;		  
    getGeneralIntersect(ls2, ELEMOF(ls2), resultg);
    for(int i = 0; i < resultg.size(); i++)
	cout << resultg[i].first << " " << resultg[i].second << endl;

    return 0;
}

