
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _point 
{
    int x,y;
}point;

typedef struct _point2
{
    point p;
    int i;
    float f;
}point2;

class ycomp
{
public:
    bool operator ()(const point2 &p1, const point2 &p2)
    {
        return p1.p.y > p2.p.y;        
    }
};

// (0,0) => (1,  0): 0 
// (0,0) => (-1, 0): 0 => 2
// (0,0) => (0,  1): 1
// (0,0) => (0, -1):-1 => 3
// (0,0) => (1,  1): 1/2  
// (0,0) => (-1, 1): 1/2 => 3/2 
// (0,0) => (-1,-1):-1/2 => 5/2 
// (0,0) => ( 1,-1):-1/2 => 7/2
float theta(point &p1, point &p2)
{
   int dx,dy,ax,ay;
   float t;

   dx = p2.x-p1.x; ax = abs(dx);
   dy = p2.y-p1.y; ay = abs(dy);

   t = (ax+ay == 0) ? 0 : ((float)dy)/(ax+ay);
   if (dx < 0) t = 2-t; 
   else if (dy < 0) t = 4+t;

   return t;
}

void findConvex(point ps[], int num)
{
    vector<point2> vp(num);
    vector<int> result;
    int first = -1;
    for(int i = 0; i< num; i++)
    {
	if (first == -1 || ps[first].y < ps[i].y) first = i;    
        vp[i].p = ps[i];
	vp[i].i = i;
	vp[i].f = 0;
    }

    cout << first << endl;
    //sort(vp.begin(), vp.end(), ycomp());
    float prevf = 0.0;
    int next = first;
    result.emplace_back(next);

    do {
        float minf = 0;
	int next2 = -1;
        for(int i = 0; i < vp.size(); i++)
	{   
	    if (i == next) continue; 
            float f = theta(vp[next].p, vp[i].p);
	    //cout << i << " " << f << endl;
	    if (f < prevf) continue;
	    if (next2 == -1 || minf > f) { minf = f; next2 = i; }
	}
      
	if (next2 == -1) { prevf = 0; continue; }
	//bool found = false;
	//for(int j=0; j < result.size(); j++) if (result[j] == next2) found = true;  
        //if (found) break;

	next = next2;
	prevf = minf;
	cout << next << "=========" << minf << endl;
	result.emplace_back(next);
    }while(next != first);

    //for(int i = 0; i < result.size(); i++)
    //    cout << result[i] << ",";
    //cout << endl;
}

int main(int argc, char* argv[])
{
    point ps[] = {{3,9},{11,1},{6,8},{4,3},{5,15},{8,11},{1,6},{7,4},
	          {9,7},{14,5},{10,13},{16,14},{15,2},{13,16},{3,12},{12,10}};

    findConvex(ps, ELEMOF(ps));
    return 0;
}
