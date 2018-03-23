

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _point 
{
    int x,y;
}point;

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
	treeNode *p = root;
	treeNode *q = root;
	while(q != NULL) { p = q; q = (p->key > key) ? p->left : p->right; }
	if (root == NULL) root = pNode;
        else { if (p->key > key) p->left = pNode; else p->right = pNode; } 
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

void printVector(vector<int> &arg, const char* title)
{
    if (title) cout << title << endl;	
    for(int i = 0; i < arg.size(); i++)
	cout << arg[i] << ",";
    cout << endl;
}

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

    return 0;
}
