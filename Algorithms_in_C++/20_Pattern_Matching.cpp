
#include <iostream>
#include <set>
#include <vector>
#include <deque>
#include <string>

using namespace std;
#define ELEMOF(x) (sizeof(x)/sizeof(x[0]))

typedef struct _element
{
    char c;
    vector<int> links;
}element;

typedef enum {
    nul = 0,	
    cat = 1,
    ore = 2,
    mul = 3,
}etag;

typedef struct _expr
{
    etag t; 
    string base;
    vector<struct _expr*> sub;
}expr;

expr* newNULexpr(vector<expr*> &all, string data)
{
    expr* e = new expr();
    e->t = nul;
    e->base = data;
    all.emplace_back(e);

    return e;
}

expr* newCATexpr(vector<expr*> &all, expr** data, int num)
{
    expr* e = new expr();
    e->t = cat;
    for(int i = 0; i< num; i++) e->sub.emplace_back(data[i]);
    all.emplace_back(e);

    return e;
}

expr* newOREexpr(vector<expr*> &all, expr** data, int num)
{
    expr* e = new expr();
    e->t = ore;
    for(int i = 0; i< num; i++) e->sub.emplace_back(data[i]);
    all.emplace_back(e);

    return e;
}

expr* newMULexpr(vector<expr*> &all, expr* data)
{
    expr* e = new expr();
    e->t = mul;
    e->sub.emplace_back(data);
    all.emplace_back(e);

    return e;
}

void increaseLink(element e, int offset)
{
    for(int i = 0; i < e.links.size(); i++) e.links[i] += offset;
}

void updateLink(vector<element> &pool, set<int> &vint, int newvalue)
{
    for(int i = 0; i < pool.size(); i++)
    {
        element &e = pool[i];
	for(int j = 0; j < e.links.size(); j++) 
	    if (vint.find(e.links[i]) != vint.end()) e.links[i] = newvalue;
    }
}

void getElements(vector<element> &pool, expr* root)
{
    pool.clear();
    switch(root->t)
    {
        case nul:
	{
	    for(int i = 0; i <= root->base.size(); i++)	
            {
                element e;
		if (i == 0) e.c = 0;
		else
		{
		    e.c = root->base[i];
		    e.links.emplace_back(i+1); 
                }
		pool.emplace_back(e);
	    }
	    break;
        }
	case cat: // remove the 0 item in non-first subexpr
	{
            int offset = 0;
	    for(int i = 0; i < root->sub.size(); i++)
	    {
                vector<element> subpool;
		getElements(subpool, root->sub[i]);
		for(int j = 0; j < subpool.size(); j++)
		{
                    increaseLink(subpool[j], offset);
		    pool.emplace_back(subpool[j]);
		}
		offset += subpool.size();
	    }
	    break;
        }
	case ore:
	{
            element e; e.c = 0; 
	    pool.emplace_back(e);
	    int offset = 1;
	    set<int> oldends;
	    for(int i = 0; i < root->sub.size(); i++)
	    {
                vector<element> subpool;
		getElements(subpool, root->sub[i]);
		for(int j = 0; j < subpool.size(); j++)
		{
                    increaseLink(subpool[j], offset);
		    pool.emplace_back(subpool[j]);
		}
		oldends.insert(pool.size());
		pool[0].links.emplace_back(offset);
		offset += subpool.size();
	    }

	    updateLink(pool, oldends, pool.size());
	    break;
	}
	case mul:
	{
	    vector<element> subpool;
	    getElements(subpool, root->sub[0]);
            element e; e.c = 0; e.links.emplace_back(1); 
	    pool.emplace_back(e);
	    for(int j = 0; j < subpool.size(); j++)
	    {
                increaseLink(subpool[j], 1);
	        pool.emplace_back(subpool[j]);
	    }
            pool[1].links.emplace_back(pool.size());
	    pool[pool.size()-1].links.emplace_back(1);
	    break;
	}    
    }
}

//(A*B+AC)D
void getexample1()
{
    vector<expr*> all;

    expr* e0 = newNULexpr(all, "A");
    expr* e1 = newMULexpr(all, e0);
    expr* e2 = newNULexpr(all, "B");
    expr* s1[] = {e1,e2};
    expr* e3 = newCATexpr(all, s1, ELEMOF(s1));

    expr* e4 = newNULexpr(all, "AC");
    expr* s2[] = {e3,e4};
    expr* e5 = newOREexpr(all, s2, ELEMOF(s2));

    expr* e6 = newNULexpr(all, "D");
    expr* s3[] = {e5,e6};
    expr* e7 = newCATexpr(all, s3, ELEMOF(s3));

    vector<element> pool;
    getElements(pool, e7);
    cout << pool.size() << endl;
    for(int i = 0; i < all.size(); i++) delete all[i];
}

//((A+B)+C)(DE)
void getexample2()
{
    vector<expr*> all;

    expr* e1 = newNULexpr(all, "A");
    expr* e2 = newNULexpr(all, "B");
    expr* s1[] = {e1,e2};
    expr* e3 = newOREexpr(all, s1, ELEMOF(s1));

    expr* e4 = newNULexpr(all, "C");
    expr* s2[] = {e3,e4};
    expr* e5 = newOREexpr(all, s2, ELEMOF(s2));

    expr* e6 = newNULexpr(all, "DE");
    expr* s3[] = {e5,e6};
    expr* e7 = newCATexpr(all, s3, ELEMOF(s3));
    
    for(int i = 0; i < all.size(); i++) delete all[i];
}

void covertToElements(int links[][2], char gates[], int num, vector<element> &pool)
{
   for(int i = 0; i < num; i++)
   {
       element e;
       e.c = gates[i];
       e.links.emplace_back(links[i][0]);
       int j = (links[i][0] != links[i][1]) ? 2 : 1; 
       e.links.assign(links[i], links[i]+j);
       pool.emplace_back(e);
   }  
  
#if 0   
   for(int i = 0; i < pool.size(); i++)
   {
       cout << i;
       for(int j = 0; j < pool[i].links.size(); j++) cout << "," << pool[i].links[j];
       cout << endl;
   }
#endif   
}

bool patternMatch(vector<element> &pool, string &test, int start, int end)
{	
    const int next = -1;	
    deque<int> d; 
    d.push_front(start);
    d.push_back(next);

    int i = 0;
    int t = 0;
    bool match = false;
    while(d.size() > 0)
    {
        t = d.front(); d.pop_front();    
	//cout << t; for(int j = 0; j < d.size(); j++) cout<< ',' << d[j]; cout << endl;
	if (t == next) { if (i < test.size()) { i++; d.push_back(next); } continue; } 
	if (t == end) { if (i == test.size()) match = true; break; }

	element &p = pool[t];
	if (p.c == 0) 
	    for(int j = 0; j <p.links.size(); j++) d.push_front(p.links[j]);
	if (p.c == test[i]) 
	    for(int j = 0; j <p.links.size(); j++) d.push_back(p.links[j]);
	//cout << t; for(int j = 0; j < d.size(); j++) cout<< ',' << d[j]; cout << endl;
    }
   
    //cout << i << " " << t << " = " << match << endl;
    return match;
}

int main(int argc, char* argv[])
{
    string pattern = "(A*B+AC)D";
    string example0 = "AAABD";
    string example1 = "AAACD";
    string example2 = "ACD";
    string example3 = "AAABDF";
    string example4 = "AAAB";
    string example5 = "BD";
    
    vector<element> pool;        
    int links1[][2] = {{1,2},{4,5},{3,3},{6,6},{5,1},{6,6},{7,7},{8,8}};
    char gates[] = { 0, 0, 'A', 'C', 'A', 'B', 0, 'D'};
    int start = 0;
    int end = ELEMOF(links1);
   
    covertToElements(links1, gates, ELEMOF(links1), pool);
    cout << example0 << ":" << patternMatch(pool, example0, start, end) << endl;
    cout << example1 << ":" << patternMatch(pool, example1, start, end) << endl;
    cout << example2 << ":" << patternMatch(pool, example2, start, end) << endl;
    cout << example3 << ":" << patternMatch(pool, example3, start, end) << endl;
    cout << example4 << ":" << patternMatch(pool, example4, start, end) << endl;
    cout << example5 << ":" << patternMatch(pool, example5, start, end) << endl;
    
    getexample1();
    getexample2();
    return 0;
}

