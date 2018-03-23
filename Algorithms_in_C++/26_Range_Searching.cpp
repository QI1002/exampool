

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _point 
{
    int x,y;
}point;

void printVector(vector<int> &arg, const char* title)
{
    if (title) cout << title << endl;	
    for(int i = 0; i < arg.size(); i++)
	cout << arg[i] << ",";
    cout << endl;
}

typedef struct _treeNode
{
    struct _treeNode* left;
    struct _treeNode* right;
    int key;
    int index;
}treeNode;

class searchTree
{
public:
    searchTree() { root = NULL; }	
    ~searchTree() { for(int i = 0; i < pool.size(); i++) delete pool[i]; } 
    void insert(int key, int index)
    {
        treeNode* pNode = new treeNode();
	pNode->left = pNode->right = NULL;
	pNode->key = key; pNode->index = index;
        pool.emplace_back(pNode);
	if (root == NULL) { root = pNode; return; }
	treeNode *p = root;
	treeNode *q = root;
	while(q != NULL) 
	{ 
	    p = q; 
	    if (p->key > key) { q = p->left; if (q == NULL) p->left = pNode; }
	    else { q = p->right; if (q == NULL) p->right = pNode; }
	}
    }

    void range(int start, int end, vector<int> &find, treeNode *p = NULL)
    {
        if (p == NULL) p = root;
	bool b1 = (p->key >= start);
	bool b2 = (p->key <= end);

	//cout << p->key << " " << b1 << " " << b2 << endl;
	if (b1 && b2) find.emplace_back(p->index);
	if (b1 && p->left != NULL) range(start, end, find, p->left); 
	if (b2 && p->right != NULL) range(start, end, find, p->right); 
    }

private:
    treeNode* root;
    vector<treeNode*> pool;
};

void rangeSearch(searchTree &xSearch, searchTree &ySearch, int left, int right, int top, int bottom, vector<int> &result)
{
    vector<int> xFind;
    vector<int> yFind;
  
    xSearch.range(left, right, xFind);    
    sort(xFind.begin(), xFind.end());
    printVector(xFind, "xfind = "); 
    
    ySearch.range(top, bottom, yFind);    
    sort(yFind.begin(), yFind.end());
    printVector(yFind, "yfind = "); 
    
    int x = 0, y = 0;
    while(x < xFind.size() && y < yFind.size())
    {
        bool b1 = xFind[x] <= yFind[y];
	bool b2 = xFind[x] >= yFind[y];
	if (b1 && b2) result.emplace_back(xFind[x]);
	if (b1) x++;
	if (b2) y++;
    }
}

typedef struct _treeNode2
{
    struct _treeNode2* left;
    struct _treeNode2* right;
    point p;
    int xy; // x: 0, y: 1
    int index;
}treeNode2;

class searchTree2
{
public:
    searchTree2() { root = NULL; }	
    ~searchTree2() { for(int i = 0; i < pool.size(); i++) delete pool[i]; } 
    void insert(point pp, int index)
    {
        treeNode2* pNode = new treeNode2();
	pNode->left = pNode->right = NULL;
	pNode->p = pp; pNode->index = index; pNode->xy = 0;
        pool.emplace_back(pNode);
	if (root == NULL) { root = pNode; return; }
	treeNode2 *p = root;
	treeNode2 *q = root;
	while(q != NULL) 
	{ 
	    int pv, v;
	    p = q;
	    
	    if (p->xy) { pv = p->p.y; v = pp.y; pNode->xy = 0; }
	    else { pv = p->p.x; v = pp.x; pNode->xy = 1; }
	    
	    if (pv > v) { q = p->left; if (q == NULL) p->left = pNode; }
	    else { q = p->right; if (q == NULL) p->right = pNode; }
	}
    }

    void range(int start[], int end[], vector<int> &find, treeNode2 *p = NULL)
    {
        if (p == NULL) p = root;
	    
	int pv = (p->xy) ? p->p.y : p->p.x;
	bool b1 = (pv >= start[p->xy]);
	bool b2 = (pv <= end[p->xy]);

	//cout << p->key << " " << b1 << " " << b2 << endl;
	if (b1 && b2) 
	{ 
	    int other = (p->xy) ? 0 : 1;
	    int ov = (p->xy) ? p->p.x : p->p.y;
	    if ((ov >= start[other]) && (ov <= end[other]))
	        find.emplace_back(p->index);
	}

	if (b1 && p->left != NULL) range(start, end, find, p->left); 
	if (b2 && p->right != NULL) range(start, end, find, p->right); 
    }

private:
    treeNode2* root;
    vector<treeNode2*> pool;
};

void rangeSearch2(searchTree2 &xySearch, int start[], int end[], vector<int> &result)
{
    xySearch.range(start, end, result);    
    sort(result.begin(), result.end());
}

int main(int argc, char* argv[])
{
    point ps[] = {{3,9},{11,1},{6,8},{4,3},{5,15},{8,11},{1,6},{7,4},
	          {9,7},{14,5},{10,13},{16,14},{15,2},{13,16},{3,12},{12,10}};

    searchTree xSearch;
    searchTree ySearch;

    for(int i = 0; i < ELEMOF(ps); i++)
    {
        xSearch.insert(ps[i].x, i);
        ySearch.insert(ps[i].y, i);
    }
    
    vector<int> result;
    int left = 2;
    int right = 10;
    int top = 3;
    int bottom = 9;
    rangeSearch(xSearch, ySearch, left, right, top, bottom, result);
    printVector(result, "result = "); 

    searchTree2 xySearch;
    vector<int> result2;
    int start[] = {left, top};
    int end[] = {right, bottom};
    for(int i = 0; i < ELEMOF(ps); i++)
        xySearch.insert(ps[i], i);
    rangeSearch2(xySearch, start, end, result2);
    printVector(result2, "result2 = "); 
    
    return 0;
}
