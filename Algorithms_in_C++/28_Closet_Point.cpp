
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _point 
{
    int x,y;
}point;

int dist2(point &p0, point &p1)
{
    return (p0.x-p1.x)*(p0.x-p1.x)+(p0.y-p1.y)*(p0.y-p1.y);
}

int findCloset(point ps[], int num, int &mini, int &minj)
{
    int min = -1;
    for(int i = 0; i < num; i++)
        for(int j = i+1; j < num; j++)
	{
	    int k = dist2(ps[i], ps[j]);	
            if (min == -1 || min > k) { min = k; mini = i; minj = j; } 
	}

    return min; 
}

int findFastCloset(vector<point> &vps, int start, int end, int &mini, int &minj)
{
    int n = end-start+1;
    int min = -1;
    if (n <= 1) return min;
    if (n == 2) { mini = start; minj = end; return dist2(vps[mini], vps[minj]); }
    
    int mini0, mini1, minj0, minj1;
    int r1 = findFastCloset(vps, start, start+n/2-1, mini0, minj0); 
    int r2 = findFastCloset(vps, start+n/2, start+n-1, mini1, minj1);
    if (r1 > 0 && (min == -1 || min > r1)) { min = r1; mini = mini0; minj = minj0; } 
    if (r2 > 0 && (min == -1 || min > r2)) { min = r2; mini = mini1; minj = minj1; } 

    if (min == -1) { cout << "error " << start << " " << end; return min; }
   
    int f  = floor(sqrt(min));	    
    int x0 = start;
    int x1 = start+n/2;
    int xm = x1-1;
    do {
	int i, xx = f+1;    
        
	for(i = x0; i <= xm; i++) 
	{
	    xx = abs(vps[i].x-vps[x1].x);	
	    if (xx <= f) break;
	}
      
	if (xx > f) break;
	x0 = i;
	for(i = x0; i <= xm; i++)
	{
            xx = dist2(vps[i],vps[x1]);
	    if (min > xx) { min = xx; mini = i; minj = x1; f = floor(sqrt(min)); } 
	}

	x1 += 1;

    }while(true);

    return min;
}

class xcomp
{
public:
    bool operator()(point &a, point &b)
    {
        return a.x < b.x;
    }
};

int main(int argc, char* argv[])
{
    point ps[] = {{3,9},{11,1},{6,8},{4,3},{5,15},{8,11},{1,6},{7,4},
	          {9,7},{14,5},{10,13},{16,14},{15,2},{13,16},{3,12},{12,10}};
    
    int mini, minj;
    mini = minj = -1;
    int d1 = findCloset(ps, ELEMOF(ps), mini, minj);
    cout << "closet point = " << ps[mini].x << "," << ps[mini].y << " " 
	                      << ps[minj].x << "," << ps[minj].y << "=" << d1 << endl;

    mini = minj = -1;
    vector<point> vps;
    vps.assign(ps, ps+ELEMOF(ps));
    sort(vps.begin(), vps.end(), xcomp());
    int d2 = findFastCloset(vps, 0, vps.size()-1, mini, minj);
    cout << "closet point = " << vps[mini].x << "," << vps[mini].y << " " 
	                      << vps[minj].x << "," << vps[minj].y << "=" << d2 << endl;
    return 0;
}
