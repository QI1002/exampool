
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

typedef struct _line 
{
    point s,e;
}line;

class fcomp
{
public:
    fcomp(vector<point2> ps) { this->ps = ps; }	
    bool operator ()(const int a, const int b)
    {
        return ps[a].f < ps[b].f;
    }

private:
    vector<point2> ps;
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

int CCW(point &p0, point &p1, point &p2)
{
    int dx1, dx2, dy1, dy2;
    
    dx1 = p1.x - p0.x; dy1 = p1.y - p0.y;
    dx2 = p2.x - p0.x; dy2 = p2.y - p0.y;
    //cout << dx1 << " " << dx2 << " " << dy1 << " " << dy2 << endl;
    if (dx1*dy2 > dy1*dx2) return 1;
    if (dx1*dy2 < dy1*dx2) return -1;
    // if equal means dx1/dy1 == dx2/dy2
    if ((dx1*dx2 < 0) || (dy1*dy2 < 0)) return -1;
    if ((dx1*dx1+dy1*dy1) < (dx2*dx2+dy2*dy2)) return 1;
    return 0;
}

// not ok when test ((0,6)(100,6)) and ((1,6)(1,6))
bool isIntersect(line l1, line l2)
{
    int ccw1 = CCW(l1.s, l1.e, l2.s);
    int ccw2 = CCW(l1.s, l1.e, l2.e);
    int ccw3 = CCW(l2.s, l2.e, l1.s);
    int ccw4 = CCW(l2.s, l2.e, l1.e);

    //cout << ccw1 << " " << ccw2 << " " << ccw3 << " " << ccw4 << endl;
    return (ccw1*ccw2 <= 0 && ccw3*ccw4 <= 0);
}

bool inLine(point p, line l)
{
    int dx1 = p.x - l.s.x;
    int dx2 = p.x - l.e.x;
    int dy1 = p.y - l.s.y;
    int dy2 = p.y - l.e.y;
    if ((dx1*dx2) <= 0 && (dy1*dy2) <= 0)
    {
        if ((dx1*dy2) == (dx2*dy1))
	{
	    //cout << p.x << " " << p.y << " " << l.s.x << " " << l.s.y << " " << l.e.x << " " << l.e.y << endl;	
	    return true;
	}
    }

    return false;		    
}

bool isInside(vector<point> &bound, point test, int xmax)
{
    line testl = { test, test };
    
    testl.e.x = 100; //xmax; // not use INT_MAX but 100 for not overflow
    int count = 0;
    
    for(int i = 1; i <= bound.size(); i++)
    {
	line edge;

	edge.e = (i == bound.size()) ? bound[0] : bound[i];
	edge.s = bound[i-1];
        if (inLine(edge.e, testl)) continue;  
        if (isIntersect(testl, edge)) count++; 
    }

    return (count & 1);
}

void testInside(point ps[], int num, vector<int> &convex)
{
    vector<point> bound;	
    vector<bool> inConvex(num, false);
    for(int i = 0; i < convex.size(); i++)
    {
	int index = convex[i];
	inConvex[index] = true;
        bound.emplace_back(ps[index]);
    }


    point left, right, top, bottom;
    right = left = bound[0];
    bottom = top = bound[0];
    for(int i = 1; i < bound.size(); i++)
    {
        if (left.x > bound[i].x) left = bound[i];
        if (right.x < bound[i].x) right = bound[i];
        if (top.y > bound[i].y) top = bound[i];
        if (bottom.y < bound[i].y) bottom = bound[i];
    }
    
    left.x--; right.x++; top.y--; bottom.y++;	    
    
    for(int i = 0; i < num; i++)
    {
        if (inConvex[i]) continue;
	cout << i << " inside = " << isInside(bound, ps[i], right.x) << endl;
    }

    cout << "left inside = " << isInside(bound, left, right.x) << endl; 
    cout << "right inside = " << isInside(bound, right, right.x) << endl; 
    cout << "top inside = " << isInside(bound, top, right.x) << endl; 
    cout << "bottom inside = " << isInside(bound, bottom, right.x) << endl; 
}


void findConvex2(point ps[], int num, vector<int> &result)
{
    vector<point2> vp(num);
    int first = -1;
    for(int i = 0; i< num; i++)
    {
	if (first == -1 || ps[first].y < ps[i].y) first = i;    
        vp[i].p = ps[i];
	vp[i].i = i;
	vp[i].f = 0;
    }

    //cout << first << endl;
    vector<int> order(num);
    for(int i = 0; i < vp.size(); i++)
    {
        vp[i].f = theta(vp[first].p, vp[i].p);
        order[i] = i;
    }
    
    sort(order.begin(), order.end(), fcomp(vp));
    for(int i = 0; i < order.size(); i++)
        cout << order[i] << ",";
    cout << endl;
    
    int s1 = order[0];
    int s2 = order[1];
    int s3 = order[2];
    result.emplace_back(s1); 
    result.emplace_back(s2); 
    int n = order.size();
    order.emplace_back(s1);
    order.emplace_back(s2);
    for(int i = 2; i < n; i++)
    {
	s1 = result[result.size()-1]; 
	s2 = order[i];
	s3 = order[i+1];
        int ccw = CCW(vp[s1].p, vp[s2].p, vp[s3].p);
	//cout << s1 << "," << s2 << "," << s3 << "," << ccw << endl;
	if (ccw == 1) result.emplace_back(s2);
	else 
	{
            do {
                s1 = result[result.size()-2];
		s2 = result[result.size()-1];
		s3 = order[i+1];
                ccw = CCW(vp[s1].p, vp[s2].p, vp[s3].p);
		if (ccw == -1) result.pop_back();
	    }while(ccw == -1);
	}
    }
}

void findConvex(point ps[], int num, vector<int> &result)
{
    vector<point2> vp(num);
    int first = -1;
    for(int i = 0; i< num; i++)
    {
	if (first == -1 || ps[first].y < ps[i].y) first = i;    
        vp[i].p = ps[i];
	vp[i].i = i;
	vp[i].f = 0;
    }

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
	    if (f < prevf) continue;
	    if (next2 == -1 || minf > f) { minf = f; next2 = i; }
	}
      
	if (next2 == -1) { prevf = 0; continue; }
        if (next2 == first) break;

	next = next2;
	prevf = minf;
	result.emplace_back(next);

    }while(true);
}

int main(int argc, char* argv[])
{
    point ps[] = {{3,9},{11,1},{6,8},{4,3},{5,15},{8,11},{1,6},{7,4},
	          {9,7},{14,5},{10,13},{16,14},{15,2},{13,16},{3,12},{12,10}};
    
    vector<int> result;
    findConvex(ps, ELEMOF(ps), result);
    for(int i = 0; i < result.size(); i++)
        cout << result[i] << ",";
    cout << endl;

    vector<int> result2;
    findConvex2(ps, ELEMOF(ps), result2);
    for(int i = 0; i < result2.size(); i++)
        cout << result2[i] << ",";
    cout << endl;
   
    cout << "====================" << endl;
    //line l1 = { ps[6], ps[6] };
    //l1.s.x = 0; l1.e.x = 100;
    //line l2 = { ps[6], ps[6] };
    //cout << inLine(ps[6], l2) << endl;
    testInside(ps, ELEMOF(ps), result);
    return 0;
}
