
//
//
//

#include <iostream>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

class node
{
    static int id;

public:	
    node(char value)	    
    {
	index = id++;    
        values.emplace_back(value);
	links.resize(2, NULL);
    }

    int index;
    vector<char> values;
    vector<node*> links;
};

int node::id = 0;

bool isTreeBalanced(node* root)
{
    deque<pair<node*,int>> d;
    d.push_front(pair<node*,int>(root,0));
    set<int> depths;

    while(d.size() > 0)
    {
        pair<node*,int> p = d.front(); d.pop_front();
	node* n = p.first; int depth = p.second;
	bool leaf = true;
        for(int i = 0; i < n->links.size(); i++) 
	    if (n->links[i] != NULL) 
	    { 
		d.push_front(pair<node*, int>(n->links[i], depth+1)); 
		leaf = false; 
	    }

	if (leaf) depths.insert(depth);
    }

    //for(auto it = depths.begin(); it != depths.end(); it++) cout << *it << ",";
    //cout << endl;

    if (depths.size() > 2) return false;
    if (depths.size() <= 1) return true;

    auto it = depths.begin();
    int a = *it; it++; int b = *it;
    return (abs(a-b) <= 1);
}

void treeDelPrint(node* root, bool del = false)
{
    deque<node*> d;
    d.push_back(root);
    
    while(d.size() > 0)
    {
        node* n = d.front(); d.pop_front();
        for(int i = 0; i < n->links.size(); i++) 
	    if (n->links[i] != NULL) d.push_back(n->links[i]);

	cout << n->index << ":";
	for(int i = 0; i < n->values.size(); i++) cout << n->values[i] << ",";
	cout << endl;

        if (del) { delete n; continue; }
    }
}

void treeInsert(node* &root, char c)
{
    if (root == NULL) { root = new node(c); return; }

    auto comp = [](int i, int j) { return i < j; };
    node *n = root;
    deque<node*> track;
    int li;

    while(n != NULL)
    {
       track.push_front(n);
       auto it = upper_bound(n->values.begin(), n->values.end(), c, comp);
       li = it - n->values.begin();
       n = n->links[li];
    }

    //cout << li << endl;
    node* t = NULL;	
    while(track.size() >0)
    {
        n = track.front(); track.pop_front();
	auto it1 = upper_bound(n->values.begin(), n->values.end(), c, comp);
        li = it1 - n->values.begin();
        n->values.emplace(it1, c);
        auto it2 = n->links.begin()+li+1;
        //cout << li << c << endl;
        n->links.emplace(it2, t); t = NULL;

        if (n->values.size() < 4) break;
        c = n->values[2];
        t = new node(n->values[3]); 
        t->links[0] = n->links[3]; 
	t->links[1] = n->links[4];
        n->values.pop_back(); n->values.pop_back();
        n->links.pop_back(); n->links.pop_back();
    }

    if (t != NULL)
    {
        root = new node(c);
	root->links[0] = n;
	root->links[1] = t;
    }

    if (isTreeBalanced(root) == false) cout << "not balanced tree" << endl;
}

int main(int argc, char* argv[])
{
    string example = "ASEARCHINGEXAMPLE";

    node* root = NULL;
    for(int i = 0; i < example.size(); i++)
        treeInsert(root, example[i]);
    
    treeDelPrint(root, true);
    return 0;
}

