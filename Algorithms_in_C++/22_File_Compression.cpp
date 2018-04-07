
//complete
//1. huffman coding 

#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

using namespace std;
#define CNUM 27
#define SIGN -1

typedef struct _record 
{
    char c;
    int freq;
    int parent;
    bool isr;
    int index;
    int left;
    int right;
    int code;
    int len;
}record;

class rcomp
{
public:
    bool operator()(const record *a, const record *b)
    {
        return a->freq > b->freq;    
    }
};

int findCoding(vector<record> &cf)
{
    priority_queue<record*, vector<record*>, rcomp> pq;	
    int oldsize = cf.size();
    // enlarge the vector will change it's element address
    for(int i = 0; i < oldsize; i++) { record p; cf.emplace_back(p); }
    for(int i = 0; i < oldsize; i++)
    {
        if (cf[i].freq == 0) continue;
	pq.push(&cf[i]);
    }

    //cout << pq.size() << endl;
    int index = oldsize;
    while(pq.size() >= 2)
    {
        record* r1 = pq.top(); pq.pop();
        record* r2 = pq.top(); pq.pop();
	cf[index] = {SIGN, r1->freq+r2->freq, -1, false, index, r1->index, r2->index, 0, 0};
	//cout << r1->freq << " " << r2->freq << " " << index << endl;
        pq.push(&cf[index]);	
	r1->parent = r2->parent = index;
	r1->isr = false; r2->isr = true;
	index++;
    }

    record *root = pq.top(); pq.pop();
    for(int i = 0; i < oldsize; i++)
    {
        if (cf[i].freq == 0) continue;
        
	int code = 0;
	int bits = 0;
	int p = i;
	while(cf[p].parent != -1) 
	{ 
	    if (cf[p].isr) code |= (1<<bits);	
	    p = cf[p].parent;
	    bits++;
        }

	//cout << i << "=" << cf[i].parent << " " << code << " " << bits << endl;
	cf[i].code = code;
	cf[i].len = bits;
    }

    return root->index;
}

void encodeStr(const char example[], vector<bool> &data, vector<record> &cf)
{
    int n = strlen(example);
    for(int i = 0; i < n; i++) 
    {
	int k = (example[i] != ' ') ? example[i]-'A'+1 : 0;
	for(int j = cf[k].len-1; j >=0; j--)
	{
	    if (cf[k].code & (1 << j)) 
		data.emplace_back(true); 
	    else 
		data.emplace_back(false);  
	}
    }
}

bool decodeStr(string &result, vector<bool> &data, vector<record> &cf, int root)
{
    result = "";
    int i = 0; 
    while(i < data.size())
    {
        int j = root;
	while(cf[j].c == SIGN)
	{
	    j = (data[i]) ? cf[j].right : cf[j].left;	
            i++;
	    if (i >= data.size()) break;
	}
       
	//cout << i << " " << j << endl;
	if (cf[j].c == SIGN) return false; 
	result += ((j == 0) ? ' ' : (char)('A'+j-1));
    }

    return true;
}

int main(int argc, char* argv[])
{
    const char example[] = "A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS"; 
    vector<record> cfreq(CNUM);
    for(int i = 0; i < CNUM; i++)
    {
       cfreq[i].c = (i == 0) ? ' ' : 'A'+i-1;
       cfreq[i].freq = cfreq[i].code = cfreq[i].len = 0;
       cfreq[i].parent = -1;
       cfreq[i].isr = false; 
       cfreq[i].left = cfreq[i].right = -1;
       cfreq[i].index = i;
    }
    
    int n = strlen(example);
    for(int i = 0; i < n; i++) if (example[i] == ' ') cfreq[0].freq++; else cfreq[example[i]-'A'+1].freq++; 
    int root = findCoding(cfreq);
    cout << "root is " << root << endl;
    for(int i = 0; i < CNUM; i++)
    {
        if (cfreq[i].freq == 0) continue;
	char c = (i == 0) ? ' ' : (char)('A'+i-1);
	cout << c;
	cout << ":" << cfreq[i].freq << ":";
	for(int j = cfreq[i].len-1; j >=0; j--) if (cfreq[i].code & (1 << j)) cout << 1; else cout << 0;  
	cout << endl;
    }

    vector<bool> data;
    encodeStr(example, data, cfreq);
    cout << "encode len = " << data.size() << endl;
    string result;
    int r = decodeStr(result, data, cfreq, root);
    cout << "decode = " << result << " with " << r << endl;

    return 0;
}
